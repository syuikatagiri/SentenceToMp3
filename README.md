# SentenceToMp3
テキストに記述された文章をMP3に変換するプログラム。

https://soundoftext.com/というWebサイトがあり、
入力された文章から「合成音声で読み上げたMP3形式のファイル」を作成してくれるWebサイトである。

MP3ファイルを作成するためには、

「Webサイト内に一つだけ存在するテキストボックスに文章を入力して、確定ボタン、DLボタンを押下する」という作業が必要で、

「大量の短い文章をMP3形式のファイルで保存」したいと思うと、
上記の作業がほしい文章の数に比例して増えていくことになる。

だから、テキストに改行区切りで格納されている文章を読み込んで、
改行区切りで一つの文章として扱い、Webサイトにアクセス、文章の入力、ボタンの押下を
自動でやってもらうために作った。

