Vue.component('todo-item', {
  template: '<li>Ceci est une liste</li>'
})

var app = new Vue({
    el: '#app-5',
    data: {
      message: "Hello Vue"
    },
    delimiters: ['[[',']]']
  })

  var app = new Vue({
    el: '#app-6',
    data: {
      message: "Is this my third app"
    },
    delimiters: ['[[',']]']
  })
