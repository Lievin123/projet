import flet as ft
from flet import *
#fonction principale contenant la page principale
def main(page:Page):
    #titre de la page
    page.title = "Convertisseur d\'unité "
    #rendre l'application adaptive
    page.adaptive = True
    page.padding = 0
    
    
    
    #fonction contenant l'application du système francophone
    def fr_event(e):
        unites = {
            "Longueur": [
                "Mètres", "Décimètres", "Centimètres", "Millimètres",
                "Kilomètres", "Hectomètres", "Décamètres",
                
            ],
            "Masse": [
                "Grammes", "Décigrammes", "Centigrammes", "Milligrammes",
                "Kilogrammes", "Hectogrammes", "Décagrammes",
                "Onces", "Livres"
            ],
            "Température": [
                "Celsius", "Fahrenheit", "Kelvin"
            ],
            "Volume": [
                "Litres", "Décilitres", "Centilitres", "Millilitres",
                "Hectolitres", "Décalitres", "Gallons", "Pintes"
            ],
            "Temps":[
                "seconde","milliseconde","microseconde","nanoseconde","minute",
                "heure","jour","semaine","mois","année"
            ],
            "Vitesse":[
                "m/s","km/h","mi/h","kn","ft/s","km/s","m/min","fur/s"
            ],
            
            "Surface" : [
            "Pied carré (ft²)",
            "Yard carré (yd²)",
            "Acre (ac)"  ],
            "Puissance" : [
                "Cheval-vapeur (hp)",
                "Watt (W)"],
            "Pression" : [
                "Livre-force par pouce carré (psi)",
                "Bar (bar)",
                "Millimètre de mercure (mmHg)"],
            "Force" : {
            "Livre-force (lbf)",
            "Newton (N)"
        }

    }
        def actualisation(e: ControlEvent) -> None:
            anchor.value = None
            resultat.value = None
            valeur.value = None
            next_united.value = None
            last_united.value = None
            last_united.error_text = None
            valeur.error_text = None
            page.update()
        #definition des thèmes de la page
        page.theme = Theme(
            color_scheme_seed=colors.BLUE_900,
            color_scheme=ColorScheme(
                primary=colors.BLUE
            ),
        )
        page.dark_theme = Theme(
            color_scheme_seed=colors.BLUE_900,
            color_scheme=ColorScheme(
                primary=colors.BLUE_900
            )
        )
        page.theme.page_transitions = PageTransitionsTheme(
            android=PageTransitionTheme.CUPERTINO,
            ios=PageTransitionTheme.CUPERTINO,
            macos=PageTransitionTheme.CUPERTINO,
            linux=PageTransitionTheme.CUPERTINO,
            windows=PageTransitionTheme.CUPERTINO
        )

        page.theme_mode = ThemeMode.LIGHT
        # le app bar de l'application
        page.appbar = ft.AppBar(
            leading=ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="système Anglophone",on_click = en_event),
                    ft.PopupMenuItem(text="À propos de l'App"),
                    ft.PopupMenuItem(text="Suggestions"),
                    ft.PopupMenuItem(text="Paramètres"),
                    ft.PopupMenuItem(text="Déconnexion"),
                    ft.PopupMenuItem(
                        text="Nous contacter", checked=False, on_click=""
                    ),
                ]
            ),
            leading_width=40,
            title=ft.Text("Convertisseur d'unités", weight='bold', color=ft.colors.BLUE_50),
            center_title=False,
            bgcolor=ft.colors.BLUE_900,
            actions=[
                ft.IconButton(
                    ft.icons.BRIGHTNESS_6_OUTLINED,
                    selected_icon=ft.icons.BRIGHTNESS_6,
                    selected=page.theme_mode == ft.ThemeMode.DARK,
                    on_click=lambda e: ((page.__setattr__("theme_mode", ft.ThemeMode.LIGHT), e.control.__setattr__("selected", False)) if page.theme_mode == ft.ThemeMode.DARK
                    else (page.__setattr__("theme_mode", ft.ThemeMode.DARK), e.control.__setattr__("selected", True)), page.update())),
                
            ],
        )
        longueur = {
        "Mètres": 1, "Décimètres": 0.1, "Centimètres": 0.01, "Millimètres": 0.001,
        "Kilomètres": 1000, "Hectomètres": 100, "Décamètres": 10,
        
        }
        puissance = {
            "Cheval-vapeur (hp)": 745.7,
            "Watt (W)": 1
        }
        surface = {
        "Pied carré (ft²)": 1,
        "Yard carré (yd²)": 9,
        "Acre (ac)": 4047 * 100  # conversion m² to ft²
        }
        pression = {
            "Livre-force par pouce carré (psi)": 1,
            "Bar (bar)": 14.5038,
            "Millimètre de mercure (mmHg)": 0.193368
        }
        Temps={
            "seconde":  1,
            "milliseconde":  0.001,
            "microseconde": 0.000001,
            "nanoseconde":  0.000000001,
            "minute": 60,
            "heure":  3600,
            "jour": 86400,
            "semaine":  604800,
            "mois": 2592000,  # approximatif
            "année": 31536000
        }
        Vitesse={
            "m/s": 1,
            "km/h": 3.6,
            "mi/h": 2.23694,
            "kn": 1.852,
            "ft/s": 0.3048,
            "km/s": 1000,
            "m/min": 0.01667,
            "fur/s": 0.3048
        }

        masses = {
            "Grammes": 1, "Décigrammes": 0.1, "Centigrammes": 0.01, "Milligrammes": 0.001,
            "Kilogrammes": 1000, "Hectogrammes": 100, "Décagrammes": 10,
            "Onces": 28.3495, "Livres": 453.592
        }
        force = {
            "Livre-force (lbf)": 1,
            "Newton (N)": 0.224809
        }
        

        temperature = {
            "Celsius": lambda x: x,
            "Fahrenheit": lambda x: (x * 9/5) + 32,
            "Kelvin": lambda x: x + 273.15
        }

        volume = {
            "Litres": 1, "Décilitres": 0.1, "Centilitres": 0.01, "Millilitres": 0.001,
            "Hectolitres": 100, "Décalitres": 10, "Gallons": 3.78541, "Pintes": 0.473176
        }
        def convertir(e):
            try:
                valeur_a_convertir = float(valeur.value)
                from_unit = last_united.value
                to_unit = next_united.value

                if anchor.value == "Longueur":
                    conversion_factor = longueur[from_unit] / longueur[to_unit]
                    converted_value = valeur_a_convertir * conversion_factor
                elif anchor.value=="Temps":
                    conversion_factor = Temps[from_unit]/Temps[to_unit]
                    converted_value=valeur_a_convertir*conversion_factor
                elif anchor.value=="Force":
                    conversion_factor = force[from_unit]/force[to_unit]
                    converted_value=valeur_a_convertir*conversion_factor
                elif anchor.value =="Vitesse":
                    conversion_factor = Vitesse[from_unit]/Vitesse[to_unit]
                    converted_value =valeur_a_convertir*conversion_factor
                elif anchor.value == "Masse":
                    conversion_factor = masses[from_unit] / masses[to_unit]
                    converted_value = valeur_a_convertir * conversion_factor
                elif anchor.value =="Surface":
                    conversion_factor = surface[from_unit]/surface[to_unit]
                    converted_value = valeur_a_convertir * conversion_factor
                elif anchor.value =="Puissance":
                    conversion_factor = puissance[from_unit]/puissance[to_unit]
                    converted_value = valeur_a_convertir * conversion_factor
                elif anchor.value =="Pression":
                    conversion_factor = pression[from_unit]/pression[to_unit]
                    converted_value = valeur_a_convertir * conversion_factor
                elif anchor.value == "Température":
                    if from_unit == "Celsius" and to_unit == "Fahrenheit":
                        converted_value = (valeur_a_convertir * 9/5) + 32
                    elif from_unit == "Celsius" and to_unit == "Kelvin":
                        converted_value = valeur_a_convertir + 273.15
                    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
                        converted_value = (valeur_a_convertir - 32) * 5/9
                    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
                        converted_value = (valeur_a_convertir - 32) * 5/9 + 273.15
                    elif from_unit == "Kelvin" and to_unit == "Celsius":
                        converted_value = valeur_a_convertir - 273.15
                    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
                        converted_value = (valeur_a_convertir - 273.15) * 9/5 + 32
                    else:
                        converted_value = valeur_a_convertir
                elif anchor.value == "Volume":
                    conversion_factor = volume[from_unit] / volume[to_unit]
                    converted_value = valeur_a_convertir * conversion_factor
                elif last_united.value == None:
                    last_united.error_text="Choisir une unité"

                resultat.value = f"{round(converted_value,3)} {next_united.value}"
                resultat.color = None
               
                resultat.update()
            except ValueError:
                last_united.error_text="Choisir une unité"
                valeur.error_text ="Erreur"
                resultat.value = ("Erreur de conversion") 
                resultat.color ="red"   
                valeur.update()
                resultat.update()
                last_united.update()


        
        #le bouton flottant sur le bottom app bar
        page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.REFRESH , on_click = actualisation  )
        page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED
        #definition du bttom app bar
        page.bottom_appbar = ft.BottomAppBar(
        bgcolor=ft.colors.BLUE_900,
        shape=ft.NotchShape.CIRCULAR,
        content=ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.HOME, icon_color=ft.colors.WHITE),
                ft.Container(expand=True),
                ft.IconButton(icon=ft.icons.SETTINGS, icon_color=ft.colors.WHITE),
                
            ]
        ),
        )
        """def masse(e: ControlEvent):
            last_united.options = [ft.dropdown.Option(option) for option in unites.get(anchor.value, [])]
            next_united.options = [ft.dropdown.Option(option) for option in unites.get(anchor.value, [])]
            last_united.update()
            next_united.update()"""
        # on definit l'input de recherche
        

        result_list = Column()
        def select_grandeur(e):
            anchor.close_view(e.control.value.title())
            last_united.options = [ft.dropdown.Option(option) for option in unites.get(anchor.value, [])]
            next_united.options = [ft.dropdown.Option(option) for option in unites.get(anchor.value, [])]
            last_united.update()
            next_united.update()
            page.update()
            
            
        def search_grandeur(query):
            result_list.controls.clear()
            for grandeur, options in unites.items():
                if query.lower() in grandeur.lower():
                    result_list.controls.append(ft.ListTile(title=ft.Text(grandeur), on_click=select_grandeur, data=grandeur))
                    anchor.update()
                else:
                    for option in options:
                        if query.lower() in option.lower():
                            result_list.controls.append(ft.ListTile(title=ft.Text(grandeur), on_click=select_grandeur, data=grandeur))
                            break
            result_list.update()

        
            
			  

        

        def close_anchor(e):
            #update_unites_dropdown()
            #print(anchor.value)
            valeur.value=""
            last_united.options = [ft.dropdown.Option(option) for option in unites.get(e.control.data, [])]
            next_united.options = [ft.dropdown.Option(option) for option in unites.get(e.control.data, [])]
            
            text = f"{e.control.data}"
            anchor.close_view(text)
            last_united.update()
            next_united.update()
            valeur.update()
            #page.update()
		 
        a = unites  
        lv = ft.ListView()  
        def handle_change(e): 
            list_to_show = [unite for unite in unites if e.data.lower() in unite.lower()]
            if list_to_show==[]: list_to_show.append("Resultat non trouve")
            lv.controls.clear()       
            lv.controls=[ft.ListTile(title=ft.Text(f"{i}",color="red" if i=="Resultat non trouve" else "black"), on_click=close_anchor, data=i)for i in list_to_show]
            anchor.update()
            
        """
        def handle_submit(e):
            anchor.value = e.control.data
            last_united.options = [ft.dropdown.Option(option) for option in unites.get(anchor.value, [])]
            next_united.options = [ft.dropdown.Option(option) for option in unites.get(anchor.value, [])]
            last_united.update()
            next_united.update()
            anchor.update()
            page.update()
            anchor.close_anchor

            """
        """def handle_search(e):
            search_grandeur(e.data)
            result_list.update()
            page.update()
            anchor.update()
            page.update()
            anchor.view.update()
            anchor.view_leading.update()"""

        anchor = ft.SearchBar(
            view_elevation=4,
            width=page.width - 150,
            full_screen=True,
            divider_color=ft.colors.AMBER,
            bar_hint_text="Recherche de grandeur...",
            view_hint_text="Choisir une grandeur...",
            on_change=handle_change,
            on_submit=select_grandeur,
            on_tap=lambda _: anchor.open_view(),
            controls=[
                lv
            ],
        )

        chercher = ft.IconButton(
            icon=icons.LIST,
            autofocus=True,
            bgcolor=colors.BLACK12,
            on_click=lambda _: anchor.open_view()
        )
        search = Row(
            controls =[anchor,chercher]
        )
        valeur = ft.TextField(
            label="Nombre",
            keyboard_type = KeyboardType.NUMBER ,
            width=90,
        )
        instruction = Text("cliquez sur l\'icon bleu ci haut pour convertir")
        
        last_united = Dropdown(
            width=200,
            label='Unité d\'entrée',
            options=[ft.dropdown.Option(option) for option in unites.get("Longueur", [])]
        )
        resultat = ft.Text(
            width=300,
            text_align = TextAlign.CENTER,
            size = 30,
            weight = 'bold',
        )
        con = ft.Container(
            height=70,
            width=300,
            padding=5,
            content=ft.Row(spacing=10, controls=[valeur, last_united])
        )
        #l'alignement du champs ou entrer le nombre à convertir et l'unité d'entrée
        #definition du select des unités de sortie
        next_united = Dropdown(
            width=220,
            label='Unité de sortie',
            options=[ft.dropdown.Option(option) for option in unites.get("Longueur" ,[])]
        )
        # definition du bouton qui permet de convertir
        btn_c = IconButton(icon=icons.ARROW_FORWARD, icon_size=50, on_click=convertir)
        conv = ft.Container(
            height=70,
            padding=5,
            content=ft.Row(spacing=10, controls=[next_united, btn_c],alignment=ft.MainAxisAlignment.CENTER,
                            )
        )
        R_mes = Text("Résultat", size = 18)
        field = ft.Container(
            border_radius=10,
            height = 300,
            width = page.width - 10,
            content=ft.Column([ con, conv,instruction],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            border=ft.border.all(0.5),
            shadow = BoxShadow(
                spread_radius= 0.7 ,
                blur_radius= 15 ,
                color= ft.colors.BLUE_100,
                blur_style=  ShadowBlurStyle.OUTER
            )
        )
        cont_result = Container(
            height = 100,
            width = page.width - 50,
            border=ft.border.all(0.5),
            shadow = BoxShadow(
                spread_radius= 0.7 ,
                blur_radius= 15 ,
                color= ft.colors.BLUE_100,
                blur_style=  ShadowBlurStyle.OUTER
            ),
            
            content=ft.Column([resultat],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        )
        
        main_fr = Container(
            expand = True,
            padding = 10,
            width = page.width,
            content = Column(scroll =True,controls = [search,field,R_mes,cont_result],alignment= MainAxisAlignment.CENTER,horizontal_alignment= CrossAxisAlignment.CENTER)
        )
        page.clean()
        page.add(main_fr)
        page.update()
    def en_event(e):
        unites = {
        "Longueur": [

            "Pouces", "Pieds", "Yards", "Miles"
        ],
        "Masse": [
            "Gram", "Décigram", "Centigram", "Milligram",
            "Kilogram", "Hectogram", "Décagram",
            "Onces", "Livres"
        ],
        "Température": [
            "Celsius", "Fahrenheit", "Kelvin"
        ],
        "Volume": [
            "Litres", "Décilitres", "Centilitres", "Millilitres",
            "Hectolitres", "Décalitres", "Gallons", "Pintes"
        ],
        "Temps":[
            "second","millisecond","microsecond","nanosecond","minute",
            "hours","day","week","month","year"
        ],
        "Vitesse":[
            "m/s","km/h","mi/h","kn","ft/s","km/s","m/min","fur/s"
        ],
        
        "Surface" : [
        "Pied carré (ft²)",
        "Yard carré (yd²)",
        "Acre (ac)"  ],
        "Puissance" : [
            "Cheval-vapeur (hp)",
            "Watt (W)"],
        "Pression" : [
            "Livre-force par pouce carré (psi)",
            "Bar (bar)",
            "Millimètre de mercure (mmHg)"],
        "force_units" : {
        "Livre-force (lbf)",
        "Newton (N)"
    }

    }
        def actualisation(e: ControlEvent) -> None:
            anchor.value = None
            resultat.value = None
            valeur.value = None
            next_united.value = None
            last_united.value = None
            last_united.error_text = None
            valeur.error_text = None
            page.update()
        #definition des thèmes de la page
        page.theme = Theme(
            color_scheme_seed=colors.RED_900,
            color_scheme=ColorScheme(
                primary=colors.RED
            ),
        )
        page.dark_theme = Theme(
            color_scheme_seed=colors.RED_900,
            color_scheme=ColorScheme(
                primary=colors.RED_900
            )
        )
        page.theme.page_transitions = PageTransitionsTheme(
            android=PageTransitionTheme.CUPERTINO,
            ios=PageTransitionTheme.CUPERTINO,
            macos=PageTransitionTheme.CUPERTINO,
            linux=PageTransitionTheme.CUPERTINO,
            windows=PageTransitionTheme.CUPERTINO
        )

        page.theme_mode = ThemeMode.LIGHT
        # le app bar de l'application
        page.appbar = ft.AppBar(
            leading=ft.PopupMenuButton(
                icon_color = colors.WHITE,
                items=[
                    ft.PopupMenuItem(text="Système Francophone", on_click = fr_event),
                    ft.PopupMenuItem(text="Signaler un bug", ),
                    ft.PopupMenuItem(text="Suggestions"),
                    ft.PopupMenuItem(text="Paramètres"),
                    ft.PopupMenuItem(
                        text="Nous contacter", checked=False, on_click=""
                    ),
                ]
            ),
            leading_width=40,
            title=ft.Text("Convertisseur d'unités", weight='bold', color=ft.colors.BLUE_50),
            center_title=False,
            bgcolor=ft.colors.RED_900,
            actions=[
                ft.IconButton(
                    ft.icons.BRIGHTNESS_6_OUTLINED,
                    icon_color = colors.WHITE,
                    selected_icon=ft.icons.BRIGHTNESS_6,
                    selected=page.theme_mode == ft.ThemeMode.DARK,
                    on_click=lambda e: ((page.__setattr__("theme_mode", ft.ThemeMode.LIGHT), e.control.__setattr__("selected", False)) if page.theme_mode == ft.ThemeMode.DARK
                    else (page.__setattr__("theme_mode", ft.ThemeMode.DARK), e.control.__setattr__("selected", True)), page.update())),
                
            ],
        )
        longueur = {
        
        "Pouces": 0.0254, "Pieds": 0.3048, "Yards": 0.9144, "Miles": 1609.34
        }
        puissance = {
            "Cheval-vapeur (hp)": 745.7,
            "Watt (W)": 1
        }
        surface = {
        "Pied carré (ft²)": 1,
        "Yard carré (yd²)": 9,
        "Acre (ac)": 4047 * 100  # conversion m² to ft²
        }
        pression = {
            "Livre-force par pouce carré (psi)": 1,
            "Bar (bar)": 14.5038,
            "Millimètre de mercure (mmHg)": 0.193368
        }
        Temps={
            "second":  1,
            "millisecond":  0.001,
            "microsecond": 0.000001,
            "nanosecond":  0.000000001,
            "minute": 60,
            "hours":  3600,
            "day": 86400,
            "week":  604800,
            "month": 2592000,  # approximatif
            "year": 31536000
        }
        Vitesse={
            "m/s": 1,
            "km/h": 3.6,
            "mi/h": 2.23694,
            "kn": 1.852,
            "ft/s": 0.3048,
            "km/s": 1000,
            "m/min": 0.01667,
            "fur/s": 0.3048
        }

        masses = {
            "Gram": 1, "Décigram": 0.1, "Centigram": 0.01, "Milligram": 0.001,
            "Kilogram": 1000, "Hectogram": 100, "Décagram": 10,
            "Onces": 28.3495, "Pound": 453.592
        }
        force = {
            "Livre-force (lbf)": 1,
            "Newton (N)": 0.224809
        }
        

        temperature = {
            "Celsius": lambda x: x,
            "Fahrenheit": lambda x: (x * 9/5) + 32,
            "Kelvin": lambda x: x + 273.15
        }

        volume = {
            "Litres": 1, "Décilitres": 0.1, "Centilitres": 0.01, "Millilitres": 0.001,
            "Hectolitres": 100, "Décalitres": 10, "Gallons": 3.78541, "Pintes": 0.473176
        }
        def convertir(e):
            try:
                valeur_a_convertir = float(valeur.value)
                from_unit = last_united.value
                to_unit = next_united.value

                if anchor.value == "Longueur":
                    conversion_factor = longueur[from_unit] / longueur[to_unit]
                    converted_value = valeur_a_convertir * conversion_factor
                elif anchor.value=="Temps":
                    conversion_factor = Temps[from_unit]/Temps[to_unit]
                    converted_value=valeur_a_convertir*conversion_factor
                elif anchor.value =="Vitesse":
                    conversion_factor = Vitesse[from_unit]/Vitesse[to_unit]
                    converted_value =valeur_a_convertir*conversion_factor
                elif anchor.value == "Masse":
                    conversion_factor = masses[from_unit] / masses[to_unit]
                    converted_value = valeur_a_convertir * conversion_factor
                elif anchor.value =="Surface":
                    conversion_factor = surface[from_unit]/surface[to_unit]
                    converted_value = valeur_a_convertir * conversion_factor
                elif anchor.value =="Puissance":
                    conversion_factor = puissance[from_unit]/puissance[to_unit]
                    converted_value = valeur_a_convertir * conversion_factor
                elif anchor.value =="Pression":
                    conversion_factor = pression[from_unit]/pression[to_unit]
                    converted_value = valeur_a_convertir * conversion_factor
                elif anchor.value == "Température":
                    if from_unit == "Celsius" and to_unit == "Fahrenheit":
                        converted_value = (valeur_a_convertir * 9/5) + 32
                    elif from_unit == "Celsius" and to_unit == "Kelvin":
                        converted_value = valeur_a_convertir + 273.15
                    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
                        converted_value = (valeur_a_convertir - 32) * 5/9
                    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
                        converted_value = (valeur_a_convertir - 32) * 5/9 + 273.15
                    elif from_unit == "Kelvin" and to_unit == "Celsius":
                        converted_value = valeur_a_convertir - 273.15
                    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
                        converted_value = (valeur_a_convertir - 273.15) * 9/5 + 32
                    else:
                        converted_value = valeur_a_convertir
                elif anchor.value == "Volume":
                    conversion_factor = volume[from_unit] / volume[to_unit]
                    converted_value = valeur_a_convertir * conversion_factor
                elif last_united.value == None:
                    last_united.error_text="Choisir une unité"

                resultat.value = f"{round(converted_value,3)} {next_united.value}"
                resultat.color = None
               
                resultat.update()
            except ValueError:
                last_united.error_text="Choisir une unité"
                valeur.error_text ="Erreur"
                resultat.value = ("Erreur de conversion") 
                resultat.color ="red"   
                valeur.update()
                resultat.update()
                last_united.update()


        
        #le bouton flottant sur le bottom app bar
        page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.REFRESH , on_click = actualisation  )
        page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED
        #definition du bttom app bar
        page.bottom_appbar = ft.BottomAppBar(
        bgcolor=ft.colors.RED_900,
        shape=ft.NotchShape.CIRCULAR,
        content=ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.HOME, icon_color=ft.colors.WHITE),
                ft.Container(expand=True),
                ft.IconButton(icon=ft.icons.SETTINGS, icon_color=ft.colors.WHITE),
                
            ]
        ),
        )
        """def masse(e: ControlEvent):
            last_united.options = [ft.dropdown.Option(option) for option in unites.get(anchor.value, [])]
            next_united.options = [ft.dropdown.Option(option) for option in unites.get(anchor.value, [])]
            last_united.update()
            next_united.update()"""
        # on definit l'input de recherche
        

        result_list = Column()
        def select_grandeur(e):
            anchor.close_view(e.control.value.title())
            last_united.options = [ft.dropdown.Option(option) for option in unites.get(anchor.value, [])]
            next_united.options = [ft.dropdown.Option(option) for option in unites.get(anchor.value, [])]
            last_united.update()
            next_united.update()
            page.update()
            
            
        def search_grandeur(query):
            result_list.controls.clear()
            for grandeur, options in unites.items():
                if query.lower() in grandeur.lower():
                    result_list.controls.append(ft.ListTile(title=ft.Text(grandeur), on_click=select_grandeur, data=grandeur))
                    anchor.update()
                else:
                    for option in options:
                        if query.lower() in option.lower():
                            result_list.controls.append(ft.ListTile(title=ft.Text(grandeur), on_click=select_grandeur, data=grandeur))
                            break
            result_list.update()

        
            
			  

        

        def close_anchor(e):
            #update_unites_dropdown()
            #print(anchor.value)
            valeur.value=""
            last_united.options = [ft.dropdown.Option(option) for option in unites.get(e.control.data, [])]
            next_united.options = [ft.dropdown.Option(option) for option in unites.get(e.control.data, [])]
            
            text = f"{e.control.data}"
            anchor.close_view(text)
            last_united.update()
            next_united.update()
            valeur.update()
            #page.update()
		 
        a = unites  
        lv = ft.ListView()  
        def handle_change(e): 
            list_to_show = [unite for unite in unites if e.data.lower() in unite.lower()]
            if list_to_show==[]: list_to_show.append("Resultat non trouve")
            lv.controls.clear()       
            lv.controls=[ft.ListTile(title=ft.Text(f"{i}",color="red" if i=="Resultat non trouve" else "black"), on_click=close_anchor, data=i)for i in list_to_show]
            anchor.update()
            
        """
        def handle_submit(e):
            anchor.value = e.control.data
            last_united.options = [ft.dropdown.Option(option) for option in unites.get(anchor.value, [])]
            next_united.options = [ft.dropdown.Option(option) for option in unites.get(anchor.value, [])]
            last_united.update()
            next_united.update()
            anchor.update()
            page.update()
            anchor.close_anchor

            """
        """def handle_search(e):
            search_grandeur(e.data)
            result_list.update()
            page.update()
            anchor.update()
            page.update()
            anchor.view.update()
            anchor.view_leading.update()"""

        anchor = ft.SearchBar(
            view_elevation=4,
            width=page.width - 150,
            full_screen=True,
            divider_color=ft.colors.AMBER,
            bar_hint_text="Recherche de grandeur...",
            view_hint_text="Choisir une grandeur...",
            on_change=handle_change,
            on_submit=select_grandeur,
            on_tap=lambda _: anchor.open_view(),
            controls=[
                lv
            ],
        )

        chercher = ft.IconButton(
            icon=icons.LIST,
            icon_color = colors.RED_600,
            autofocus=True,
            bgcolor=colors.BLACK12,
            on_click=lambda _: anchor.open_view()
        )
        search = Row(
            controls =[anchor,chercher]
        )
        valeur = ft.TextField(
            label="Nombre",
            keyboard_type = KeyboardType.NUMBER ,
            width=90,
        )
        instruction = Text("cliquez sur l\'icon bleu ci haut pour convertir")
        
        last_united = Dropdown(
            width=200,
            label='Unité d\'entrée',
            options=[ft.dropdown.Option(option) for option in unites.get("Longueur", [])]
        )
        resultat = ft.Text(
            width=300,
            text_align = TextAlign.CENTER,
            size = 30,
            weight = 'bold',
        )
        con = ft.Container(
            height=70,
            width=300,
            padding=5,
            content=ft.Row(spacing=10, controls=[valeur, last_united])
        )
        #l'alignement du champs ou entrer le nombre à convertir et l'unité d'entrée
        #definition du select des unités de sortie
        next_united = Dropdown(
            width=220,
            label='Unité de sortie',
            options=[ft.dropdown.Option(option) for option in unites.get("Longueur" ,[])]
        )
        # definition du bouton qui permet de convertir
        btn_c = IconButton(icon=icons.ARROW_FORWARD,icon_color = 'red', icon_size=50, on_click=convertir)
        conv = ft.Container(
            height=70,
            padding=5,
            content=ft.Row(spacing=10, controls=[next_united, btn_c],alignment=ft.MainAxisAlignment.CENTER,
                            )
        )
        R_mes = Text("Résultat", size = 18)
        field = ft.Container(
            border_radius=10,
            height = 300,
            width = page.width - 10,
            content=ft.Column([ con, conv,instruction],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            border=ft.border.all(0.5),
            shadow = BoxShadow(
                spread_radius= 0.7 ,
                blur_radius= 15 ,
                color= ft.colors.BLUE_100,
                blur_style=  ShadowBlurStyle.OUTER
            )
        )
        cont_result = Container(
            height = 100,
            width = page.width - 50,
            border=ft.border.all(0.5),
            shadow = BoxShadow(
                spread_radius= 0.7 ,
                blur_radius= 15 ,
                color= ft.colors.BLUE_100,
                blur_style=  ShadowBlurStyle.OUTER
            ),
            
            content=ft.Column([resultat],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        )
        
        main_en = Container(
            expand = True,
            padding = 10,
            width = page.width,
            content = Column(scroll =True,controls = [search,field,R_mes,cont_result],alignment= MainAxisAlignment.CENTER,horizontal_alignment= CrossAxisAlignment.CENTER)
        )
        page.clean()
        page.add(main_en)
        page.update()
    
    fr = ElevatedButton("Système francophone",icon = icons.LOGIN,width = 350,height = 40,style = ButtonStyle(shape=RoundedRectangleBorder(radius=10)),bgcolor = colors.BLUE_900,color = colors.WHITE, on_click = fr_event)
    en = ElevatedButton("Système Anglophone",icon = icons.LOGIN,width = 350,height = 40,style = ButtonStyle(shape=RoundedRectangleBorder(radius=10)),bgcolor = colors.RED_900,color = colors.WHITE, on_click = en_event)
    c = Container(
        expand = True,
        padding = 15,
        width = page.width,
        bgcolor =ft.colors.WHITE,
        gradient= LinearGradient(
            begin = alignment.top_center,
            end = alignment.bottom_center,
            colors=[ft.colors.BLUE_200,ft.colors.RED_100 ,ft.colors.PINK_100,] 
            ),
        content = Column(spacing = 20,controls =[fr,en],alignment= MainAxisAlignment.CENTER ,horizontal_alignment= CrossAxisAlignment.CENTER )
    )
    page.add(c)
app(target = main)