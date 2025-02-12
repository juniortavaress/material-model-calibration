import os
import yaml

class SetLayout:
    def change_page(self, page):
        # print("page", page)
        if page == 0:
            self.ui.frame_105.hide()
            self.resize(1000, 600)
            self.ui.button_result.setEnabled(False)
            self.ui.button_settings_next_page.setEnabled(False)
            self.ui.pages.setCurrentIndex(0)
        elif page == 1:
            self.ui.pages.setCurrentIndex(1)
        elif page == 2:
            self.ui.pages.setCurrentIndex(2)
        elif page == 3:
            self.ui.pages.setCurrentIndex(3)
        elif page == 4:
            self.ui.pages.setCurrentIndex(4)
        elif page == 5:
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







