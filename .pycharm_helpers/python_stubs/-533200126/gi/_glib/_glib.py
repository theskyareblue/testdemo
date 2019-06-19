# encoding: utf-8
# module gi._glib._glib
# from /usr/lib64/python2.7/site-packages/gi/_glib/_glib.so
# by generator 1.145
# no doc
# no imports

# functions

def spawn_async(argv, envp=None, working_directory=None, flags=0, child_setup=None, user_data=None, standard_input=None, standard_output=None, standard_error=None): # real signature unknown; restored from __doc__
    """
    spawn_async(argv, envp=None, working_directory=None,
                flags=0, child_setup=None, user_data=None,
                standard_input=None, standard_output=None,
                standard_error=None) -> (pid, stdin, stdout, stderr)
    Execute a child program asynchronously within a glib.MainLoop()
    See the reference manual for a complete reference.
    """
    pass

def threads_init(): # real signature unknown; restored from __doc__
    """
    threads_init()
    Initialize GLib for use from multiple threads. If you also use GTK+
    itself (i.e. GUI, not just PyGObject), use gtk.gdk.threads_init()
    instead.
    """
    pass

# classes

class GError(RuntimeError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    message = None


class OptionContext(object):
    # no doc
    def add_group(self, *args, **kwargs): # real signature unknown
        pass

    def get_help_enabled(self, *args, **kwargs): # real signature unknown
        pass

    def get_ignore_unknown_options(self, *args, **kwargs): # real signature unknown
        pass

    def get_main_group(self, *args, **kwargs): # real signature unknown
        pass

    def parse(self, *args, **kwargs): # real signature unknown
        pass

    def set_help_enabled(self, *args, **kwargs): # real signature unknown
        pass

    def set_ignore_unknown_options(self, *args, **kwargs): # real signature unknown
        pass

    def set_main_group(self, *args, **kwargs): # real signature unknown
        pass

    def _get_context(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass


class OptionGroup(object):
    # no doc
    def add_entries(self, *args, **kwargs): # real signature unknown
        pass

    def set_translation_domain(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass


class Pid(int):
    # no doc
    def close(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class PollFD(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    revents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

_PyGLib_API = None # (!) real value is ''

