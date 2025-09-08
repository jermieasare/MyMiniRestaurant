from nicegui import ui
def render():
    """Creates the menu page with a hero section."""
    with ui.column().classes('w-full'):
        # Menu Page Hero Section
        with ui.column().classes('relative w-full h-[400px] flex items-center justify-center bg-gray-800'):
            with ui.element("div").style("background-image: url(/assets/menu_image1.jpg)").classes("h-screen w-screen bg-cover bg-center flex flex-col justify-center items-center"):
             ui.label('DISCOVER OUR MENU').classes('relative z-10 text-5xl font-bold text-white')
        
        # You can add the actual menu content here
        ui.label('Our delicious menu items will be displayed here.').classes('w-full text-center py-12 text-gray-600')