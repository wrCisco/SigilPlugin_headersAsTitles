# SigilPlugin_headersAsTitles
Add/modify the title tag of xhtml selected files using for each file the first most elevated h* tag in the code.

The plugin will parse the code of each selected file in search of an h1 tag, then of an h2 and so on until h6. At the first occurrence it will stop and use the text of matched tag to create/overwrite the title tag in the head of the document. If no occurrences will be found the title tag will be empty.

If you want to add/overwrite title tags of all xhtml files, just don't select any file in the Book Browser (or select them all, it's the same).
