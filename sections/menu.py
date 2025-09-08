from nicegui import ui
def render():
    """Creates the menu page with a hero section."""
    with ui.column().classes('w-full'):
        # Menu Page Hero Section
        with ui.column().classes('relative w-full h-[400px] flex items-center justify-center bg-gray-800'):
            ui.image('https://images.unsplash.com/photo-1549447330-47b2c01994e4?q=80&w=2787&auto=format&fit=crop').classes('absolute inset-0 w-full h-full object-cover opacity-70')
            ui.label('PlatedBy JM MENU').classes('relative z-10 text-5xl font-bold text-white')
        
        # You can add the actual menu content here
        ui.label('Our delicious menu items will be displayed here.').classes('w-full text-center py-12 text-gray-600')