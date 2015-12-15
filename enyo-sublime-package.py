import sublime, sublime_plugin

class enyoJSAttributeCompletion(sublime_plugin.EventListener):

	def __init__(self):
		self.settings = sublime.load_settings('enyo-completions.sublime-settings')

	def on_query_completions(self, view, prefix, locations):
		# Only trigger within JS
		if not view.match_selector(locations[0],
				'source.js'):
			return []

		return self.completions()

	def completions(self):
		core_compl = [tuple(attr) for attr in self.settings.get('completions_list')]
		extended_compl = [tuple(attr) for attr in self.settings.get('extended_completions_list')]
		extended_compl += core_compl
		return (extended_compl, sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS)
