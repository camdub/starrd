from flask.ext.assets import Bundle

js_all = Bundle('js/selectize.min.js', 'js/salvattore.min.js', 'js/starrd.js', output='app.js')

less = Bundle('less/app.less',
              'less/selectize/selectize.default.less',
              filters='less', output='css/starrd.css')

css_all = Bundle('css/normalize.css', less, output='css/app.css')
