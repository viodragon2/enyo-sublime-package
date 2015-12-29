Enyo JS Sublime Package
===

Installation Options
---
* [Download](https://github.com/viodragon2/enyo-sublime-package/archive/master.zip) this repo, rename it to 'enyo-sublime-package', and place it within your `Packages` folder. This can be found within Sublime Text at `Preferences > Browse Packages…`
* Clone the repo into your `Packages` folder `git clone git@github.com:viodragon2/enyo-sublime-package.git`

Enyo JS Auto-Completions
---

######Reserved words
* kind
* mixins

######`enyo/UIComponent` properties
* name
* id
* owner
* componentOverrides

######`enyo/Control` properties
* classes
* style
* content
* defaultKind
* tag
* allowHtml
* renderOnShow
* canGenerate
* showing

###### life cycle methods
* create
* rendered
* destroy
* constructor
* constructed

###### blocks
* components
* computed
* observers
* bindings
* events
* handlers

Enyo JS Build
---
### Requirements
Install [enyo-dev tool](https://github.com/enyojs/enyo-dev/), and make sure it's available in `PATH`.

### Build Scripts
Default is `epack` command.

Other availble variants are :
* `epack --clean`
* `enyo init`

Completions Settings
---
`Preferences > Package Settings > Enyo > Completions - User`

####Extension
You can extend or override the default completions provided by specifying `extended_completions_list`

##### Example
````
{
    "extended_completions_list":[
        ["my_completion\tMy Completion", "my-completion: '${1:string}'$0"],
    ]
}
````

#### Enable/Disable
In case you want to turn off auto completion, you may disable it by setting `disable_completions` to `true`. The default value is `false`.

````
{
    disable_completions: true
}
````
