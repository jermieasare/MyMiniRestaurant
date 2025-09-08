from nicegui import ui,app
from sections import hero, welcome,menu

#expose the assests folder to the nicegui server
app.add_static_files("/assets", "assets")

#add font awesome for social media icons
ui.add_head_html('''
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />
''')

ui.add_head_html('<link rel="stylesheet" href="/assets/reset.css">')

hero.render()
welcome.render()
menu.render()

ui.run()