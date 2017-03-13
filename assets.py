from flask_assets import Bundle

def getAssets():
    bundles = { 
        'common_css': Bundle(
            'css/ext/bootstrap.min.css',
            'css/thin_scroll.css',
            'css/common.css',
            output='public/common.css',
            filters='cssmin'),
        'common_js': Bundle(
            'js/ext/jquery.min.js',
            'js/ext/bootstrap.min.js',
            output='public/common.js',
            filters='jsmin'),

        'home_css': Bundle(
            'css/home.css',
            output='public/home.css',
            filters='cssmin'),
        'home_js': Bundle(
            'js/home.js',
            output='public/home.js',
            filters='jsmin'),

        '3Dviewer_css': Bundle(
            'css/3Dviewer.css',
            output='public/3Dviewer.css',
            filters='cssmin'),
        '3Dviewer_js': Bundle(
            'js/3Dviewer.js',
            output='public/3Dviewer.js',
            filters='jsmin')
    }
    return bundles
