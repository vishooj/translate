# google-cloud-translate==1.3.1


def translate(text):
    # [START translate_quickstart]
    # Imports the Google Cloud client library
    from google.cloud import translate

    # Instantiates a client
    translate_client = translate.Client()

    # The text to translate

    # The target language
    target = 'en'

    # Translates some text into Russian
    translation = translate_client.translate(
        text,
        target_language=target)

    print(translation)
    # print(u'Text: {}'.format(text))
    # print(u'Translation: {}'.format(translation['translatedText']))
    # [END translate_quickstart]
    return translation['translatedText']


if __name__ == '__main__':
    import os
    # os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "C:\\Users\\admin\\Downloads\\338243e517d6.json"
    print(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])

    text = u'''Adobe Acrobat PDF Files
    Adobe® Portable Document Format (PDF) is a universal file format that preserves all
    of the fonts, formatting, colours and graphics of any source document, regardless of
    the application and platform used to create it.
    Adobe PDF is an ideal format for electronic document distribution as it overcomes the
    problems commonly encountered with electronic file sharing.
    • Anyone, anywhere can open a PDF file. All you need is the free Adobe Acrobat
    Reader. Recipients of other file formats sometimes can't open files because they
    don't have the applications used to create the documents.
    • PDF files always print correctly on any printing device.
    • PDF files always display exactly as created, regardless of fonts, software, and
    operating systems. Fonts, and graphics are not lost due to platform, software, and
    version incompatibilities.
    • The free Acrobat Reader is easy to download and can be freely distributed by
    anyone.
    • Compact PDF files are smaller than their source files and download a
    page at a time for fast display on the Web.'''

    translate(text)
