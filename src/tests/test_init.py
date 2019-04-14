# -*- coding: utf-8 -*-
"""
    unittest for sphinxjp.themes.gopher
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :author: tell-k <ffk2005@gmail.com>
    :copyright: tell-k. All Rights Reserved.
"""


class TestGetPath(object):

    def _get_target(self):
        from sphinxjp.themes.gopher import get_path
        return get_path

    def _call_fut(self, *args, **kwargs):
        return self._get_target()(*args, **kwargs)

    def test_it(self):
        from sphinxjp.themes import gopher
        assert gopher.template_path == self._call_fut()


class TestSetup(object):

    def _get_target(self):
        from sphinxjp.themes.gopher import setup
        return setup

    def _call_fut(self, *args, **kwargs):
        return self._get_target()(*args, **kwargs)

    def test_it(self):

        class DummyApp:

            def add_html_theme(self, theme, template_path):
                self.theme = theme
                self.template_path = template_path

        dummy_app = DummyApp()
        self._call_fut(dummy_app)

        assert dummy_app.theme == "gopher"
        assert dummy_app.template_path != ""
