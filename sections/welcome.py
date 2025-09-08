from nicegui import ui

#holder URL for the Welcome section image
WELCOME_IMAGE = 'assets/welcome image.jpg'

def render():
 with ui.column().classes('w-full flex-col items-center py-16 px-4 md:flex-row md:space-x-8 md:px-12'):
        # Left side - text content
        with ui.column().classes('w-full md:w-1/2 items-center md:items-start text-center md:text-left'):
            ui.label('GHANAIAN RESTAURANT').classes('text-2xl font-light text-blue mt-2')
            ui.label('AKWAABA').classes('text-6xl font-light')
            ui.label('''Discover Ghana's finest flavors where tradition meets modern taste. At PlatedBy Jermie, authentic Ghanaian cuisine is reimagined for today’s food lovers.''').classes('mt-4 text-gray-700 leading-relaxed')
            ui.link('OUR STORY', '#').classes('mt-6 text-blue-500 font-semibold border-b-2 border-blue-500 pb-1')

        # Right side - image
        with ui.column().classes('w-full md:w-1/2 mt-8 md:mt-0'):
            ui.image(WELCOME_IMAGE).classes('rounded-lg shadow-lg object-cover w-full h-auto transition duration-300 ease-in-out transform hover:scale-110')