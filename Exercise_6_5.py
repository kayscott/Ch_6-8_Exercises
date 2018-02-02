text = 'X-DSPAM-Confidence: 0.8475'
pos = text.find('0')
text1 = text[pos:pos + 7]
print float(text1)