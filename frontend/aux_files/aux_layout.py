import yaml

class SetLayout:
    def change_page(self, page):
        # print("page", page)
        if page == 0:
            # self.ui.frame_35.setMaximumSize(200, 200)
            # self.ui.frame_72.setMaximumSize(200, 200)
            # self.ui.frame_106.setMaximumSize(200, 200)
            # self.ui.frame_161.setMaximumSize(200, 200)
            # self.ui.frame_results_graph.resize(200, 200)

            # self.resize(500, 500)
            self.ui.pages.setCurrentIndex(0)

        elif page == 1:
            self.ui.pages.setCurrentIndex(1)
        elif page == 2:
            self.ui.pages.setCurrentIndex(2)
        elif page == 3:
            self.ui.pages.setCurrentIndex(3)
        elif page == 4:
            # self.ui.frame_35.setMaximumSize(16777215, 16777215)
            self.ui.pages.setCurrentIndex(4)
        elif page == 5:
            # self.ui.frame_72.setMaximumSize(16777215, 16777215)
            self.ui.pages.setCurrentIndex(5)
        elif page == 6:
            self.ui.pages.setCurrentIndex(6)
        elif page == 7:
            # self.ui.frame_106.setMaximumSize(16777215, 16777215)
            self.ui.pages.setCurrentIndex(7)
        elif page == 8:
            self.ui.pages.setCurrentIndex(8)
        elif page == 9:
            self.ui.pages.setCurrentIndex(9)


    def enable_properties(self):
        if self.ui.pages.currentIndex() == 4:
            self.ui.frame_material_model.hide()
            self.ui.frame_damage_model.hide()

            with open(self.project_infos_path, "r", encoding="utf-8") as file:
                data = yaml.safe_load(file)

            material_properties = data["Material Properties"]

            for material, properties in material_properties.items():
                for property_name, value in properties.items():
                    if value == True:
                        if self.ui.comboBox_material.findText(material) == -1:
                            self.ui.comboBox_material.addItem(material)
                        self.ui.comboBox_material.setCurrentIndex(self.ui.comboBox_material.findText(material))

                        if property_name == "Plastic":
                            self.ui.frame_material_model.show()

                        elif property_name == "Damage Evolution" or property_name == "Damage Initiation":
                            self.ui.frame_damage_model.show()



