import sublime, sublime_plugin, json

class EvalcommandCommand(sublime_plugin.TextCommand):
	def run(self, view):
		filename = sublime.packages_path() + '/ulpsnt/functions.json'
		with open(filename, encoding='utf-8') as data_file:    
			self.data = json.load(data_file)
		word = self.view.substr(self.view.word(self.view.sel()[0]))

		if word in self.data:
			self.data[word]
			self.view.show_popup('<html> <body>' + self.data[word]["variants"][0]["returntype"] + '<b> ' +
					self.data[word]["variants"][0]["syntax"] + '</b><br>' + 
					self.data[word]["variants"][0]["returns"] + '<br>' + 
					self.data[word]["variants"][0]["description"] + '</body> </html>', max_width=1000)
		

