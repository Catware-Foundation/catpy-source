# NOAA Sunrise/Sunset Calculations
# **THIS CODE WAS NOT WRITTEN BY NOAA AND IS NOT SUPPORTED BY NOAA**
#
# Ported to Python from https://www.esrl.noaa.gov/gmd/grad/solcalc/main.js
# Retrieved 2019.12.24
# port by Alex Shafer (github.com/ashafer01)
#
# Summary of changes:
#  - Partial PEP-8 compliance
#  - calculate() returns two datetime objects
#  - Eliminated custom functions that are library/built-ins in Python
#  - Removed functions and code paths that seem disused/unreachable in original JS
#  - Removed all code not needed when not rendering the NOAA UI
#
# LICENSING:
#  - No licensing information is available with the original code.
#  - This port may be distributed provisionally under the terms of the MIT License,
#    however this cannot be guaranteed in perpetuity in the case that NOAA should
#    opt to make a licensing claim against this work in the future.
#  - Author of this port makes no copyright claim
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from datetime import datetime
from math import sin, cos, radians, asin, acos, degrees, floor, tan


def dsin(deg):
    return sin(radians(deg))


def dcos(deg):
    return cos(radians(deg))


def mins_to_hms(min_val):
    h, mf = divmod(min_val, 60)
    m, sf = divmod(mf * 60, 60)
    s = round(sf)
    return int(h), int(m), s


def calculate(lat, lng, time_mins, day, month, year, tz_offset_hours):
    jday = get_jd(day, month, year)
    total = jday + time_mins/1440.0 - tz_offset_hours/24.0
    T = calc_time_julian_cent(total)
    rise = calc_sunrise_set(1, T, jday, lat, lng, tz_offset_hours)
    set = calc_sunrise_set(0, T, jday, lat, lng, tz_offset_hours)

    # rise and set are in terms of minutes since midnight at this point

    rise_h, rise_m, rise_s = mins_to_hms(rise)
    set_h, set_m, set_s = mins_to_hms(set)

    return datetime(year, month, day, rise_h, rise_m, rise_s), datetime(year, month, day, set_h, set_m, set_s)


def is_leap_year(yr):
    return (yr % 4 == 0 or yr % 100 != 0) or yr % 400 == 0


def get_jd(day, month, year):
    if month <= 2:
        year -= 1
        month += 12
    A = floor(year/100)
    B = 2 - A + floor(A/4)
    JD = floor(365.25*(year + 4716)) + floor(30.6001*(month+1)) + day + B - 1524.5
    return JD


def calc_time_julian_cent(jd):
    T = (jd - 2451545.0)/36525.0
    return T


def calc_sun_eq_of_center(t):
    m = calc_geom_mean_anomaly_sun(t)
    mrad = radians(m)
    sinm = sin(mrad)
    sin2m = sin(2*mrad)
    sin3m = sin(3*mrad)
    C = sinm * (1.914602 - t * (0.004817 + 0.000014 * t)) + sin2m * (0.019993 - 0.000101 * t) + sin3m * 0.000289
    return C  # in degrees


def calc_sun_true_long(t):
    l0 = calc_geom_mean_long_sun(t)
    c = calc_sun_eq_of_center(t)
    O = l0 + c
    return O  # in degrees


def calc_sun_apparent_long(t):
    o = calc_sun_true_long(t);
    omega = 125.04 - 1934.136 * t
    lmbda = o - 0.00569 - 0.00478 * dsin(omega)
    return lmbda  # in degrees


def calc_sun_declination(t):
    e = calc_obliquity_correction(t)
    lmbda = calc_sun_apparent_long(t)

    sint = dsin(e) * dsin(lmbda)
    theta = degrees(asin(sint))
    return theta  # in degrees


def calc_hour_angle_sunrise(lat, solarDec):
    latRad = radians(lat);
    sdRad = radians(solarDec);
    HAarg = dcos(90.833) / (cos(latRad)*cos(sdRad)) - tan(latRad) * tan(sdRad)
    HA = acos(HAarg)
    return HA  # in radians (for sunset, use -HA)


def calc_sunrise_sunset_utc(rise, t, JD, latitude, longitude):
    eqTime = calc_equation_of_time(t)
    solarDec = calc_sun_declination(t)
    hourAngle = calc_hour_angle_sunrise(latitude, solarDec)
    if not rise:
        hourAngle *= -1
    delta = longitude + degrees(hourAngle)
    timeUTC = 720 - (4.0 * delta) - eqTime  # in minutes
    return timeUTC


def calc_jd_of_next_prev_rise_set(next, rise, t, JD, latitude, longitude, tz):
    julianday = JD;
    increment = 1.0 if next else -1.0

    for _ in range(365):
        try:
            time = calc_sunrise_sunset_utc(rise, t, julianday, latitude, longitude)
            break
        except ValueError:
            julianday += increment
    else:
        raise Exception('No rise/set this year at location')

    timeLocal = time + tz * 60.0
    while (timeLocal < 0.0) or (timeLocal >= 1440.0):
        incr = 1 if timeLocal < 0 else -1
        timeLocal += (incr * 1440.0)
        julianday -= incr
    return julianday;


def calc_doy_from_jd(jd):
    z = floor(jd + 0.5)
    f = (jd + 0.5) - z
    if z < 2299161:
        A = z
    else:
        alpha = floor((z - 1867216.25)/36524.25)
        A = z + 1 + alpha - floor(alpha/4)
    B = A + 1524
    C = floor((B - 122.1)/365.25)
    D = floor(365.25 * C)
    E = floor((B - D)/30.6001)
    day = B - D - floor(30.6001 * E) + f
    month = E - 1 if E < 14 else E - 13
    year = C - 4716 if month > 2 else C - 4715

    k = 1 if is_leap_year(year) else 2
    doy = floor((275 * month)/9) - k * floor((month + 9)/12) + day -30;
    return doy;


def calc_sunrise_set(rise, T, JD, latitude, longitude, timezone):
    # rise = 1 for sunrise, 0 for sunset
    try:
        time_utc = calc_sunrise_sunset_utc(rise, T, JD, latitude, longitude);
        new_time_utc = calc_sunrise_sunset_utc(rise, T, JD + time_utc/1440.0, latitude, longitude); 
        time_local = new_time_utc + (timezone * 60.0)
        return time_local
    except ValueError:
        doy = calc_doy_from_jd(JD)
        if ((latitude > 66.4) and (doy > 79) and (doy < 267)) or ((latitude < -66.4) and ((doy < 83) or (doy > 263))):
            if rise:
                jdy = calc_jd_of_next_prev_rise_set(0, rise, JD, T, latitude, longitude, timezone)
            else:
                jdy = calc_jd_of_next_prev_rise_set(1, rise, JD, T, latitude, longitude, timezone)
        else:
            if rise:
                jdy = calc_jd_of_next_prev_rise_set(1, rise, JD, T, latitude, longitude, timezone)
            else:
                jdy = calc_jd_of_next_prev_rise_set(0, rise, JD, T, latitude, longitude, timezone)
        return jdy

def calc_mean_obliquity_of_ecliptic(t):
    seconds = 21.448 - t*(46.8150 + t*(0.00059 - t*(0.001813)))
    e0 = 23.0 + (26.0 + (seconds/60.0))/60.0
    return e0  # in degrees


def calc_obliquity_correction(t):
    e0 = calc_mean_obliquity_of_ecliptic(t)
    omega = 125.04 - 1934.136 * t
    e = e0 + 0.00256 * dcos(omega)
    return e  # in degrees


def calc_geom_mean_long_sun(t):
    L0 = 279.46646 + t * (36000.76983 + t*(0.0003032))
    L0 = L0 % 360
    return L0  # in degrees


def calc_eccentricity_earth_orbit(t):
    e = 0.016708634 - t * (0.000042037 + 0.0000001267 * t)
    return e  # unitless


def calc_geom_mean_anomaly_sun(t):
    M = 357.52911 + t * (35999.05029 - 0.0001537 * t)
    return M  # in degrees


def calc_equation_of_time(t):
    epsilon = calc_obliquity_correction(t)
    l0 = radians(calc_geom_mean_long_sun(t))
    e = calc_eccentricity_earth_orbit(t)
    m = calc_geom_mean_anomaly_sun(t)

    y = tan(radians(epsilon)/2.0)
    y *= y

    sin2l0 = sin(2.0 * l0)
    sinm = dsin(m)
    cos2l0 = cos(2.0 * l0)
    sin4l0 = sin(4.0 * l0)
    sin2m = sin(2.0 * m)

    Etime = y * sin2l0 - 2.0 * e * sinm + 4.0 * e * y * sinm * cos2l0 - 0.5 * y * y * sin4l0 - 1.25 * e * e * sin2m
    return degrees(Etime)*4.0  # in minutes of time
