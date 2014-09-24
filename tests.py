try:
    from unittest import mock
except ImportError:
    import mock
import unittest

from giferror import GIFError


class Tests(unittest.TestCase):

    @mock.patch("giferror.webbrowser.open")
    def test_non_gif(self, mock_open):
        msg = "I didn't know you liked to get wet http://onelson.org/hey.png"
        with self.assertRaises(GIFError):
            raise GIFError(msg)

        mock_open.assert_not_called()

    @mock.patch("giferror.webbrowser.open")
    def test_no_link(self, mock_open):
        msg = "It's not what you know, it's what you can prove."
        with self.assertRaises(GIFError):
            raise GIFError(msg)

        mock_open.assert_not_called()

    @mock.patch("giferror.webbrowser.open")
    def test_gif(self, mock_open):
        a_gif = "http://ewdurbin.net/boom.gif"
        msg = "%s. That's how it starts." % a_gif
        with self.assertRaises(GIFError):
            raise GIFError(msg)

        mock_open.assert_called_with(a_gif)

    @mock.patch("giferror.webbrowser.open")
    def test_https_gif(self, mock_open):
        a_gif = "https://nolan.org/monte_carlo.gif"
        msg = "SHU program. %s 23-hour lockdown." % a_gif
        with self.assertRaises(GIFError):
            raise GIFError(msg)

        mock_open.assert_called_with(a_gif)

    @mock.patch("giferror.webbrowser.open")
    def test_no_message(self, mock_open):
        with self.assertRaises(GIFError):
            raise GIFError

        mock_open.assert_not_called()


if __name__ == "__main__":
    unittest.main()
