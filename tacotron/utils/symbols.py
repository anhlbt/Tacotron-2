# -*- coding: utf-8 -*-
'''
Defines the set of symbols used in text input to the model.

The default is a set of ASCII characters that works well for English or text that has been run
through Unidecode. For other data, you can modify _characters. See TRAINING_DATA.md for details.
'''
from . import cmudict

_pad        = '_'
_eos        = '~'
# _characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!\'\"(),-.:;? ' # English

_characters = "AĂÂBCDĐEÊGHIKLMNOÔƠPQRSTUƯVXYFJWZÁẮẤÉẾÍÓỐỚÚỨÝÀẰẦÈỀÌÒỒỜÙỪỲẢẲẨẺỂỈỎỔỞỦỬỶÃẴẪẼỄĨÕỖỠŨỮỸẠẶẬẸỆỊỌỘỢỤỰỴaăâbcdđeêghiklmnoôơpqrstuưvxyfjwzáắấéếíóốớúứýàằầèềìòồờùừỳảẳẩẻểỉỏổởủửỷãẵẫẽễĩõỗỡũữỹạặậẹệịọộợụựỵ!(),-.:;? \'\""

# Prepend "@" to ARPAbet symbols to ensure uniqueness (some are the same as uppercase letters):
#_arpabet = ['@' + s for s in cmudict.valid_symbols]

# Export all symbols:
symbols = [_pad, _eos] + list(_characters) #+ _arpabet


'''
How to build model for Vietnamese and English text together?
I repair symbol character to
characters = "AĂÂBCDĐEÊGHIKLMNOÔPQRSTUƯVXYFJWZÁẮẤÉẾÍÓỐỚÚỨÝÀẰẤÈỀÌÒỒỜÙỪỲẢẲẨẺỂỈỎỔỞỦỬỶÃẴẪẼỄĨÕỖỠŨỮỸẠẶẬẸỆỊỌỘỢỤỰỴaăâbcdđeêghiklmnoôpqrstuưvxyfjwzáắấéếíóốớúứýàằấèềìòồờùừỳảẳẩẻểỉỏổởủửỷãẵẫẽễĩõỗỡũữỹạặậẹệịọộợụựỵ!(),-.:;? \'\""
and cleaners='basic_cleaners'
I hope that it is useful for multi language


ầầầầ
'''