from nicegui import ui, app


def render():
    #big container
    with ui.element("div").style("background-image: url(/assets/hero.image1.jpg)").classes("h-screen w-screen bg-cover bg-center flex flex-col justify-center items-center"):
        #navbar
        with ui.element("nav").classes("flex flex-row justify-between items-center w-full fixed left-0 top-0 px-20 py-10"): 
            #logo
            ui.label("JERM").classes("text-white font-bold text-2xl")
            #navlinks
            navlinks=[{"title":"Home", "url":"/"},
                      {"title":"Menu", "url":"/menu"},
                      {"title":"Reservations", "url":"/reservations"},
                      {"title":"About", "url":"/about"},
                      {"title":"Contact", "url":"/contact"}]
            with ui.row():
                for item in navlinks:
                    ui.link(item["title"], item["url"]).classes("no-underline uppercase font-bold text-black")
            #social media icons
            with ui.row().classes("text-black"):
                ui.html("<i class='fab fa-facebook fa-1x'></i>")
                ui.html("<i class='fab fa-twitter fa-1x'></i>")
                ui.html("<i class='fab fa-instagram fa-1x'></i>")
        # text
        with ui.element("div").classes("text-white font-bold text-center"):
            ui.label("Welcome to").classes("text-2xl")
            ui.html("<h1>Jermie's Arena</h1>").classes("text-5xl")
            ui.button("Make a Reservation",color="white-800").classes("text-blue")