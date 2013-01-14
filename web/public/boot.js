require.config({
  paths: {
    jQuery: '/js/libs/jquery',
    Underscore: '/js/libs/underscore',
    Backbone: '/js/libs/backbone',
    models: 'models',
    text: '/js/libs/text',
    templates: '../templates',
    bootstrap: '/js/libs/bootstrap/js/boostrap.min.js'
  },

  shim: {
    'Backbone': ['Underscore', 'jQuery']
  }
});