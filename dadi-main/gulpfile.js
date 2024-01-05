let preprocessor = 'sass';
const {src, dest, parallel, series, watch} = require('gulp'),
    browserSync = require('browser-sync').create(),
    concat = require('gulp-concat'),
    uglify = require('gulp-uglify'),
    sass = require('gulp-sass')(require('sass')),
    autoprefixer = require('gulp-autoprefixer'),
    cleancss = require('gulp-clean-css'),
    pug = require('gulp-pug'),
    babel = require('gulp-babel'),
    ttf2woff = require('gulp-ttf2woff'),
    ttf2woff2 = require("gulp-ttftowoff2"),
    changed = require('gulp-changed'),
    image = require('gulp-imagemin'),
    webp = require('gulp-webp'),
    rename = require('gulp-rename'),
    gulpAvif = require('gulp-avif'),
    imageResize = require('gulp-image-resize');

const arraySrc = {
    "img": {
        "src": 'src/images/**/*',
        "dest": 'app/img/',
    },
    "fonts": {
        "src": 'src/fonts/**/*.ttf',
        "dest": 'app/fonts/',
    },
    "gif": {
        "src": 'src/gif/**/*.gif',
        "dest": 'app/gif/',
    },
    "video": {
        "src": 'src/video/**/*.{mov,avi,mp4}',
        "dest": 'app/video/',
    },
};

function optimizeImage() {
    return src(arraySrc.img.src)
        .pipe(changed('app/img'))
        .pipe(image({
            progressive: true
        }))
        .pipe(dest(arraySrc.img.dest))
        .pipe(browserSync.stream())
}

function webpImage() {
    return src(arraySrc.img.src)
        .pipe(changed('app/img'))
        .pipe(webp())
        .pipe(dest(arraySrc.img.dest))
        .pipe(browserSync.stream())
}

function avifImage() {
    return src(arraySrc.img.src)
        .pipe(gulpAvif())
        .pipe(dest(arraySrc.img.dest))
        .pipe(browserSync.stream())
}

function resizeImage() {
    return [400, 500, 700, 900, 1100, 1300, 1500, 1700, 1920].forEach(function (size) {
        src('src/_images/**/*')
            .pipe(changed('src/_images/**/*'))
            .pipe(imageResize({width: size}))
            .pipe(rename(function (path) {
                path.basename = `${path.basename}@${size}w`;
            }))
            .pipe(dest(arraySrc.img.src))
            .pipe(browserSync.stream())
    });
}


function woff() {
    return src([
        arraySrc.fonts.src,
    ])
        .pipe(changed('app/fonts', {
            extension: '.woff',
        }))
        .pipe(ttf2woff())
        .pipe(dest(arraySrc.fonts.dest))
        .pipe(browserSync.stream())
}

function woff2() {
    return src([
        arraySrc.fonts.src,
    ])
        .pipe(changed('app/fonts', {
            extension: '.woff2',
        }))
        .pipe(ttf2woff2())
        .pipe(dest(arraySrc.fonts.dest))
        .pipe(browserSync.stream())
}

function pugg() {
    return src([
        'src/pug/pages/**/*.pug',
    ])
        .pipe(pug({pretty: true}))
        .pipe(dest('app/'))
        .pipe(browserSync.stream())
}

function pugg2() {
    return src([
        'src/pug/includes/**/*.pug',
    ])
        .pipe(pug({pretty: true}))
        .pipe(dest('app/includes/'))
        .pipe(browserSync.stream())
}

function pug_to_php() {
    return src([
        'src/pug/pages/**/*.pug',
    ])
        .pipe(pug({pretty: true}))
        .pipe(rename({
            extname: '.php'
        }))
        .pipe(dest('src/php'))
        .pipe(browserSync.stream())
}

function php_send_app() {
    return src([
        'src/php/**/*.php',
    ])
        .pipe(dest('app'))
        .pipe(browserSync.stream())
}

function gif() {
    return src([
        arraySrc.gif.src,
    ])
        .pipe(dest(arraySrc.gif.dest))
        .pipe(browserSync.stream())
}

function video() {
    return src([
        arraySrc.video.src,
    ])
        .pipe(dest(arraySrc.video.dest))
        .pipe(browserSync.stream())
}

function browsersync() {
    browserSync.init({
        server: {baseDir: 'app/'},
        notify: false,
        online: true
    })
}

function scripts() {
    return src([
        'node_modules/vanilla-lazyload/dist/lazyload.min.js',
        // 'node_modules/imask/dist/imask.js',
        // 'node_modules/gsap/dist/gsap.min.js',
        // 'node_modules/gsap/dist/ScrollTrigger.min.js',
        'node_modules/swiper/swiper-bundle.js',
        // 'node_modules/gsap/dist/gsap.min.js',
        // 'node_modules/gsap/dist/ScrollTrigger.min.js',
        'node_modules/nouislider/dist/nouislider.min.js',
        // 'node_modules/loading-attribute-polyfill/dist/loading-attribute-polyfill.umd.js',
        'src/js/main.js',
    ])
        .pipe(babel({
            presets: ['@babel/preset-env']
        }))
        .pipe(uglify({toplevel: true}))
        .pipe(dest('app/js/libs/'))
        .pipe(concat('script.min.js'))
        .pipe(dest('app/js/'))
        .pipe(browserSync.stream())
}

function startwatch() {
    watch(['src/images/**/*'], optimizeImage);
    watch(['src/images/**/*'], webpImage);
    // watch(['src/images/**/*'], avifImage);
    watch(['src/gif/**/*.gif'], gif);
    watch(['src/fonts/**/*.ttf'], woff);
    watch(['src/fonts/**/*.ttf'], woff2);
    watch(['src/js/**/*.js', '!src/js/**/*.min.js'], scripts);
    watch(['src/pug/pages/**/*.pug', 'src/pug/includes/**/*.pug', 'src/pug/includes/**/*.pug'], pugg);
    watch(['src/pug/pages/**/*.pug', 'src/pug/includes/**/*.pug', 'src/pug/includes/**/*.pug'], pugg2);
    // watch(['src/pug/pages/**/*.pug'], pug_to_php);
    // watch(['src/php/**/*.php'], php_send_app);
    watch('src/' + preprocessor + '/**/*', styles);
    watch('src/' + preprocessor + '/**/*', styles_part);
    watch('src/**/*.html').on('change', browserSync.reload);
}

function styles() {
    return src('src/' + preprocessor + '/main.' + preprocessor)
        .pipe(eval(preprocessor)())
        .pipe(concat('style.min.css'))
        .pipe(autoprefixer({grid: true}))
        .pipe(cleancss({level: {1: {specialComments: 0}}/* , format: 'beautify' */}))
        .pipe(dest('app/css/'))
        .pipe(browserSync.stream())
}

function styles_part() {
    return src([
        'src/' + preprocessor + '/**/*.' + preprocessor,
    ], {ignore: 'src/' + preprocessor + '/common/**/*.' + preprocessor})
        .pipe(eval(preprocessor)())
        .pipe(autoprefixer({grid: true}))
        .pipe(cleancss({level: {1: {specialComments: 0}}/* , format: 'beautify' */}))
        .pipe(dest('app/css/parts/'))
        .pipe(browserSync.stream())
}

exports.browsersync = browsersync;
exports.scripts = scripts;
exports.styles = styles_part;
exports.styles = styles;
exports.pugg = pugg;
exports.pugg2 = pugg2;
exports.gif = gif;
exports.video = video;
// exports.pug_to_php = pug_to_php;
// exports.php_send_app = php_send_app;
exports.woff = woff;
exports.woff2 = woff2;
exports.optimizeImage = optimizeImage;
exports.webpImage = webpImage;
exports.avifImage = avifImage;

exports.default = parallel(pugg, pugg2, optimizeImage, webpImage, gif, video, woff, woff2, styles_part, styles, scripts, browsersync, startwatch);