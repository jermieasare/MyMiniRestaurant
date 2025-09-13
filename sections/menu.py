from nicegui import ui

def render():
    """Creates the menu page with a hero section, image carousel, and food grid."""
    with ui.column().classes('w-full menu-section'):
        # Menu Page Hero Section with Carousel
        with ui.column().classes('relative w-full h-[500px] flex items-center justify-center bg-gray-800'):
            # Carousel images
            carousel_images = [
                '/assets/menu_image1.jpg',
                '/assets/menu_image2.jpg',  # Assuming you have these images
                '/assets/menu_image3.jpg',  # Assuming you have these images
            ]
            
            # Create a simple carousel using NiceGUI's built-in carousel component
            with ui.carousel().classes('w-full h-full'):
                for img_src in carousel_images:
                    with ui.carousel_slide().classes('w-full h-full relative'):
                        # Background image
                        ui.element('div')\
                            .style(f"background-image: url({img_src})")\
                            .classes("absolute inset-0 bg-cover bg-center")
                        
                        # Overlay and text
                        ui.element('div').classes('absolute inset-0 bg-black bg-opacity-40')
                        with ui.column().classes('absolute inset-0 flex flex-col items-center justify-center'):
                            ui.label('DISCOVER OUR MENU').classes('text-5xl font-bold text-white mb-4')
                            ui.label('Authentic Ghanaian Cuisine').classes('text-2xl text-white')

        
        # Menu Grid Section
        with ui.column().classes('w-full max-w-7xl mx-auto px-4 py-16'):
            ui.label('OUR SPECIALTIES').classes('text-4xl font-bold text-center mb-2')
            ui.label('Authentic Ghanaian Cuisine').classes('text-xl text-gray-600 text-center mb-12')
            
            # Food categories tabs
            with ui.tabs().classes('w-full flex justify-center mb-8') as tabs:
                ui.tab('All').classes('text-lg font-medium')
                ui.tab('Main Dishes').classes('text-lg font-medium')
                ui.tab('Sides').classes('text-lg font-medium')
                ui.tab('Desserts').classes('text-lg font-medium')
                ui.tab('Drinks').classes('text-lg font-medium')
            
            # Food items grid
            with ui.tab_panels(tabs, value='All').classes('w-full'):
                # All foods panel
                with ui.tab_panel('All'):
                    create_food_grid([
                        {'name': 'Jollof Rice', 'price': '$15', 'image': '/assets/jollof.jpg', 'description': 'Spicy rice dish cooked with tomatoes and aromatic spices'},
                        {'name': 'Waakye', 'price': '$14', 'image': '/assets/waakye.jpg', 'description': 'Rice and beans dish served with special waakye sauce'},
                        {'name': 'Banku & Tilapia', 'price': '$18', 'image': '/assets/banku.jpg', 'description': 'Fermented corn dough with grilled tilapia and pepper sauce'},
                        {'name': 'Fufu & Light Soup', 'price': '$16', 'image': '/assets/fufu.jpg', 'description': 'Pounded cassava and plantain with spicy soup'},
                        {'name': 'Kelewele', 'price': '$8', 'image': '/assets/kelewele.jpg', 'description': 'Spicy fried plantains seasoned with ginger and spices'},
                        {'name': 'Red Red', 'price': '$12', 'image': '/assets/red_red.jpg', 'description': 'Black-eyed peas stew with fried plantain'},
                    ])
                
                # Main dishes panel
                with ui.tab_panel('Main Dishes'):
                    create_food_grid([
                        {'name': 'Jollof Rice', 'price': '$15', 'image': '/assets/jollof.jpg', 'description': 'Spicy rice dish cooked with tomatoes and aromatic spices'},
                        {'name': 'Waakye', 'price': '$14', 'image': '/assets/waakye.jpg', 'description': 'Rice and beans dish served with special waakye sauce'},
                        {'name': 'Banku & Tilapia', 'price': '$18', 'image': '/assets/banku.jpg', 'description': 'Fermented corn dough with grilled tilapia and pepper sauce'},
                        {'name': 'Fufu & Light Soup', 'price': '$16', 'image': '/assets/fufu.jpg', 'description': 'Pounded cassava and plantain with spicy soup'},
                    ])
                
                # Sides panel
                with ui.tab_panel('Sides'):
                    create_food_grid([
                        {'name': 'Kelewele', 'price': '$8', 'image': '/assets/kelewele.jpg', 'description': 'Spicy fried plantains seasoned with ginger and spices'},
                        {'name': 'Tatale', 'price': '$7', 'image': '/assets/tatale.jpg', 'description': 'Sweet plantain pancakes with a hint of spice'},
                    ])
                
                # Desserts panel
                with ui.tab_panel('Desserts'):
                    create_food_grid([
                        {'name': 'Sobolo', 'price': '$5', 'image': '/assets/sobolo.jpg', 'description': 'Hibiscus drink with pineapple and spices'},
                        {'name': 'Hausa Koko', 'price': '$6', 'image': '/assets/hausa_koko.jpg', 'description': 'Spiced millet porridge served with koose'},
                    ])
                
                # Drinks panel
                with ui.tab_panel('Drinks'):
                    create_food_grid([
                        {'name': 'Palm Wine', 'price': '$7', 'image': '/assets/palm_wine.jpg', 'description': 'Traditional fermented palm sap'},
                        {'name': 'Sobolo', 'price': '$5', 'image': '/assets/sobolo.jpg', 'description': 'Hibiscus drink with pineapple and spices'},
                    ])

def create_food_grid(food_items):
    """Create a grid of food items"""
    with ui.grid(columns=3).classes('w-full gap-6'):
        for item in food_items:
            with ui.card().classes('w-full overflow-hidden transition-all duration-300 hover:shadow-lg'):
                # Food image
                ui.image(item['image']).classes('w-full h-48 object-cover')
                
                # Food details
                with ui.card_section().classes('p-4'):
                    with ui.row().classes('justify-between items-center'):
                        ui.label(item['name']).classes('text-xl font-bold')
                        ui.label(item['price']).classes('text-lg font-bold text-blue-600')
                    
                    ui.label(item['description']).classes('text-gray-600 mt-2')
                    
                    # Add to cart button
                    with ui.row().classes('justify-end mt-4'):
                        ui.button('Add to Cart', on_click=lambda item=item: ui.notify(f"{item['name']} added to cart"))\
                            .classes('bg-blue-600 text-white hover:bg-blue-700 transition-colors')\
                            .props('flat')