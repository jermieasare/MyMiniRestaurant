from nicegui import ui, app


def render():
    ui.header().classes('flex flex-row items-center justify-between w-full p-4 bg-white bg-opacity-70 backdrop-blur-md shadow-sm')
    #big container
    with ui.element("div").style("background-image: url(/assets/hero_image1.jpg)").classes("h-screen w-screen bg-cover bg-center flex flex-col justify-center items-center"):
        #navbar
        with ui.element("nav").classes("flex flex-row justify-between items-center w-full fixed left-0 top-0 px-20 py-10"): 
            #logo
            with ui.row().classes('items-center space-x-2'):
                ui.label('PlatedBy').classes('text-2xl font-bold text-gray-800')
                ui.label('JERMIE').classes('text-s font-light text-gray-600 tracking-widest')
            #navlinks
            with ui.row().classes('md:flex items-center space-x-6'):
                ui.link('HOME', '#').classes('text-sm font-semibold text-gray-700 hover:text-red-700 no-underline')
                ui.link('MENU', '#').classes('text-sm font-semibold text-gray-700 hover:text-red-700 no-underline')
                ui.link('RESERVATION', '#').classes('text-sm font-semibold text-gray-700 hover:text-red-700 no-underline')
                ui.link('GALLERY', '#').classes('text-sm font-semibold text-gray-700 hover:text-red-700 no-underline')
                ui.link('ABOUT', '#').classes('text-sm font-semibold text-gray-700 hover:text-red-700 no-underline')
                ui.link('BLOG', '#').classes('text-sm font-semibold text-gray-700 hover:text-red-700 no-underline')
                ui.link('CONTACT', '#').classes('text-sm font-semibold text-gray-700 hover:text-red-700 no-underline')
            #social media icons
            with ui.row().classes("text-black"):
                ui.html("<i class='fab fa-facebook fa-1x'></i>")
                ui.html("<i class='fab fa-twitter fa-1x'></i>")
                ui.html("<i class='fab fa-instagram fa-1x'></i>")
            # Mobile menu button (placeholder)
            #ui.icon('menu').classes('md:hidden')

        # Hero Section
        with ui.element('div').classes('relative w-full h-full flex flex-col items-center justify-center'):
            with ui.column().classes('absolute left-1/2 -translate-x-1/2 z-10 items-center justify-center space-y-4 text-white text-center mt-6'):
                ui.label('Welcome to').classes('font-bold text-3xl md:text-4xl mb-2')
                ui.label('Platedby JERMIE').classes('text-4xl md:text-6xl font-bold text-indigo-400 mb-4 tracking-wider')
                ui.button('LOOK MENU', on_click=lambda: ui.notify('Menu clicked')).classes('mt-4 px-8 py-3 rounded-full border-2 border-white text-white font-semibold hover:bg-white hover:text-gray-800 transition-colors')
                
