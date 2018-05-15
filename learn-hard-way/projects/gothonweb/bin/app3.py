import web

urls = (
	'/hello', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")

class Index(object):
	def GET(self):
		return render.hello_form()

	def POST(self):
		form = web.input(name="Nobody", greet="Hello")
		if form.name == '':
			form.name = 'Nobody'
		if form.greet == '':
			form.greet = 'Hello'
		greeting = "%s, %s" % (form.greet, form.name)
		return render.index(greeting = greeting)

if __name__ == "__main__":
	app.run()
