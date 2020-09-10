### 下载各种依赖以及解码器

- ffmpeg

`wget https://ffmpeg.org/releases/ffmpeg-4.2.4.tar.gz`

- yasm

`wget http://www.tortall.net/projects/yasm/releases/yasm-1.3.0.tar.gz`
    
- x264

`git clone https://code.videolan.org/videolan/x264.git`

- fdk-acc

`wget https://managedway.dl.sourceforge.net/project/opencore-amr/fdk-aac/fdk-aac-2.0.1.tar.gz`

- ame

`wget http://ufpr.dl.sourceforge.net/project/lame/lame/3.99/lame-3.99.5.tar.gz`


- opus

`wget http://downloads.xiph.org/releases/opus/opus-1.1.tar.gz`

- ogg

`wget http://downloads.xiph.org/releases/ogg/libogg-1.3.2.tar.gz`

- vorbis

`wget http://downloads.xiph.org/releases/vorbis/libvorbis-1.3.5.tar.gz`

- libvpx

`git clone https://github.com/webmproject/libvpx.git`

- xvidcore

`wget http://downloads.xvid.org/downloads/xvidcore-1.3.4.tar.gz`

- libtheora

`wget http://downloads.xiph.org/releases/theora/libtheora-1.1.1.tar.gz`


### 安装
- Yasm

    tar zxvf yasm-1.3.0.tar.gz
    
    cd yasm-1.3.0
    
    ./configure --prefix=/usr/local/cellar/ffmpeg_build --bindir=/usr/bin
    
    make && make install

- x264

    cd x264
    
    ./configure --prefix=/usr/local/cellar/ffmpeg_build --bindir=/usr/bin --enable-shared
    
    make && make install

- fdk-acc

    tar zxvf fdk-aac-2.0.1.tar.gz
    
    cd fdk-aac-2.0.1
    
    autoreconf -fiv
    
    ./configure --prefix=/usr/local/cellar/ffmpeg_build --disable-shared
    
    make && make install


- Lame

    tar zxvf lame-3.99.5.tar.gz
    
    cd tar zxvf lame-3.99.5

    ./configure --prefix=/usr/local/cellar/ffmpeg_build --bindir=/usr/bin --disable-shared --enable-nasm

    make && make install

 
- Opus

    tar zxvf opus-1.1.tar.gz

    cd opus-1.1

    autoreconf -fiv

    ./configure --prefix=/usr/local/cellar/ffmpeg_build --disable-shared

    make && make install

- ogg

    tar zxvf libogg-1.3.2.tar.gz

    cd tar zxvf libogg-1.3.2

    ./configure --prefix=/usr/local/cellar/ffmpeg_build --disable-shared

    make && make install

 
- vorbis

    tar zxvf libvorbis-1.3.5.tar.gz

    cd libvorbis-1.3.5

    ./configure --prefix=/usr/local/cellar/ffmpeg_build --with-ogg=/usr/local/cellar/ffmpeg_build --disable-shared

    make && make install

 
- Libvpx

    cd libvpx

    ./configure --prefix=/usr/local/cellar/ffmpeg_build --disable-examples

    make && make install

 
- Xvidcore
    tar zxvf xvidcore-1.3.4.tar.gz

    cd xvidcore/build/generic/

    ./configure --prefix=/usr/local/cellar/ffmpeg_build

    make && make install

 
- Libtheora

    tar zxvf libtheora-1.1.1.tar.gz

    cd libtheora-1.1.1

    ./configure --prefix=/usr/local/cellar/ffmpeg_build --with-ogg=/usr/local/cellar/ffmpeg_build --disable-examples --disable-shared --disable-sdltest --disable-vorbistest

    make && make install

 
- Freetype

    tar zxvf freetype-2.3.5.tar.gz 

    cd  freetype-2.3.5

    ./configure --prefix=/usr/local/cellar/ffmpeg_build

    make && make install
    

### 安装FFMPEG

        tar zxvf ffmpeg-4.2.4.tar.gz`
        cd ffmpeg-4.2.4
        export PKG_CONFIG_PATH=/usr/local/cellar/ffmpeg_build/lib/pkgconfig
        CFLAGS="-fPIC -m64" ./configure --prefix=/usr/local/cellar/ffmpeg --enable-libx264 --enable-libfdk_aac --enable-gpl --enable-nonfree --enable-libvorbis --enable-libopus --enable-libmp3lame --enable-libfreetype --enable-pthreads  --enable-pic  --enable-bzlib --enable-zlib --enable-version3 --bindir=/usr/bin --extra-cflags="-I/usr/local/cellar/ffmpeg_build/include" --extra-ldflags="-L/usr/local/cellar/ffmpeg_build/lib"  --pkg-config-flags="--static"`
        make && make install 

### 一些错误
- `./ffmpeg: error while loading shared libraries: libx264.so.138: cannot open shared object file`
- 解决
        
        解决方法：
        vi /etc/ld.so.conf
        添加/usr/local/cellar/ffmpeg_build/lib，如下
        
            include ld.so.conf.d/*.conf
            /usr/local/cellar/ffmpeg_build/lib

        执行 ldconfig


