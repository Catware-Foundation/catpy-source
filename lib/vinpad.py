def vinpad(text):
    if text.endswith('а'):
        text = text[:-1]
        text = text + 'у'
    if text.endswith('я'):
        text = text[:-1]
        text = text + 'ю'
    if text.endswith('й'):
        text = text[:-1]
        text = text + 'я'
    if text.endswith('к'):
        text = text + 'а'
    if text.endswith('ц'):
        text = text + 'а'
    if text.endswith('к'):
        text = text + 'а'
    if text.endswith('н'):
        text = text + 'а'
    if text.endswith('г'):
        text = text + 'а'
    if text.endswith('ш'):
        text = text + 'а'
    if text.endswith('щ'):
        text = text + 'а'
    if text.endswith('з'):
        text = text + 'а'
    if text.endswith('х'):
        text = text + 'а'
    if text.endswith('ф'):
        text = text + 'а'
    if text.endswith('ы'):
        text = text + 'ов'
    if text.endswith('в'):
        text = text + 'а'
    if text.endswith('п'):
        text = text + 'а'
    if text.endswith('р'):
        text = text + 'а'
    if text.endswith('о'):
        text = text[:-1]
        text = text + 'а'
    if text.endswith('л'):
        text = text + 'а'
    if text.endswith('д'):
        text = text + 'а'
    if text.endswith('ж'):
        text = text + 'а'
    if text.endswith('ч'):
        text = text + 'а'
    if text.endswith('с'):
        text = text + 'а'
    if text.endswith('м'):
        text = text + 'а'
    if text.endswith('т'):
        text = text + 'а'
    if text.endswith('ь'):
        text = text[:-1]
        text = text + 'я'
    if text.endswith('б'):
        text = text + 'а'
    return str(text)