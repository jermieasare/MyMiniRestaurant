from nicegui import ui, app

def scroll_to_section(section_name):
    """Function to scroll to a specific section by class name"""
    ui.run_javascript(f'document.querySelector(".{section_name}").scrollIntoView({{behavior: "smooth"}})')

def render():
    
    #big container - full screen background
    with ui.element("div").style("background-image: url(/assets/hero_image1.jpg); background-size: cover; background-position: center; background-attachment: fixed; min-height: 100vh;").classes("h-screen w-full flex flex-col justify-center items-center hero-section relative"):
        #navbar - enhanced transparent mirror effect
        with ui.element("nav").classes("flex flex-row justify-between items-center w-full fixed left-0 top-0 px-20 py-2 z-50 bg-transparent backdrop-blur-lg"):#.style("backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);"): 
            #logo
            with ui.element('div').classes('flex flex-col items-center justify-center w-16 h-16 text-blue-7'):
                ui.label('PlatedBy').classes('text-xs font-light')
                ui.label('JERMIE').classes('text-base font-bold')

            #navlinks
            with ui.row().classes('md:flex items-center space-x-6'):
                ui.button('HOME', on_click=lambda: scroll_to_section('hero-section')).classes('text-sm font-semibold text-black hover:text-red-700 no-underline bg-transparent mirror-effect px-3 py-2')
                ui.button('MENU', on_click=lambda: scroll_to_section('menu-section')).classes('text-sm font-semibold text-black hover:text-red-700 no-underline bg-transparent mirror-effect px-3 py-2')
                ui.button('RESERVATION', on_click=lambda: ui.notify('Reservation coming soon')).classes('text-sm font-semibold text-black hover:text-red-700 no-underline bg-transparent mirror-effect px-3 py-2')
                ui.button('GALLERY', on_click=lambda: ui.notify('Gallery coming soon')).classes('text-sm font-semibold text-black hover:text-red-700 no-underline bg-transparent mirror-effect px-3 py-2')
                ui.button('ABOUT', on_click=lambda: scroll_to_section('about-section')).classes('text-sm font-semibold text-black hover:text-red-700 no-underline bg-transparent mirror-effect px-3 py-2')
                ui.button('BLOG', on_click=lambda: ui.notify('Blog coming soon')).classes('text-sm font-semibold text-black hover:text-red-700 no-underline bg-transparent mirror-effect px-3 py-2')
                ui.button('CONTACT', on_click=lambda: scroll_to_section('contact-section')).classes('text-sm font-semibold text-black hover:text-red-700 no-underline bg-transparent mirror-effect px-3 py-2')
            
            #social media icons
            with ui.row().classes("text-black space-x-4"):
                ui.html("<a href='#' class='text-black hover:text-red-700 transition-all duration-300'><i class='fab fa-facebook fa-lg'></i></a>")
                ui.html("<a href='#' class='text-black hover:text-red-700 transition-all duration-300'><i class='fab fa-twitter fa-lg'></i></a>")
                ui.html("<a href='#' class='text-black hover:text-red-700 transition-all duration-300'><i class='fab fa-instagram fa-lg'></i></a>")

        # Hero Section
        with ui.element('div').classes('text-white font-bold text-center bg-black/50 w-full h-full flex flex-col items-center justify-center'):
                ui.label('Welcome to').classes('font-bold text-3xl md:text-5xl mb-4')
                ui.label('PlatedBy JERMIE').classes('text-4xl md:text-7xl font-bold text-blue-6 mb-4 tracking-wider')
                ui.button('LOOK MENU', on_click=lambda: scroll_to_section('menu-section')).classes('mt-4 px-8 py-3 rounded-full text-blue-6 hover:bg-blue-600 hover:text-white transition-all duration-300').props("color=white")
                
