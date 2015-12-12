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
		core_attrs = [tuple(attr) for attr in self.settings.get('core_attribute_list')]
		extended_attrs = [tuple(attr) for attr in self.settings.get('extended_attribute_list')]
		extended_attrs += core_attrs
		return (extended_attrs, sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS)
