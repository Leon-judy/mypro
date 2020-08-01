from app_xueqiu.commons.app import App


class TestOptionStock:
    def setup_class(self):
        self.main = App().start().goto_main()

    def test_option_stock(self):
        search = self.main.goto_market().goto_search()
        search.search("海康威视")
        assert search.is_choose("海康威视")
