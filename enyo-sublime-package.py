import sublime, sublime_plugin

class EnyoJS:
	def init(self):
		self.settings = sublime.load_settings('enyo-completions.sublime-settings')

	def completions(self):
		core_compl = [tuple(attr) for attr in self.settings.get('completions_list')]
		extended_compl = [tuple(attr) for attr in self.settings.get('extended_completions_list')]
		extended_compl += core_compl
		return (extended_compl, sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS)

class enyoJSAttributeCompletion(sublime_plugin.EventListener):
	global enyo

	def on_query_completions(self, view, prefix, locations):
		if enyo.settings.get('disable_completions'):
			return []
		# Only trigger within JS
		if not view.match_selector(locations[0],
				'source.js - string.quoted - comment - meta.brace.square'):
			return []

		return enyo.completions()

enyo = EnyoJS()

def plugin_loaded():
	enyo.init()