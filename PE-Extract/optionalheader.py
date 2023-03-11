import lief

class OptionalHeader (object):

    def __init__ (self, opt_header: lief.PE.OptionalHeader = None) -> None:
        self.__magic: hex = 0x0000
        self.__maj_link_ver: int = 0
        self.__min_link_ver: int = 0
        self.__code_size = None
        self.__init_data_size = None
        self.__unint_data_size = None
        self.__code_base = None
        self.__dll_properties: lief.PE.DLL_CHARACTERISTICS = None
        # Headers were passed in, extract relevant information
        if opt_header is not None:
            self.setup (opt_header)


    def setup (self, opt_header: lief.PE.OptionalHeader) -> None:
        self.extract_magic            (opt_header)
        self.extract_maj_link_ver     (opt_header)
        self.extract_min_link_ver     (opt_header)
        self.extract_code_size        (opt_header)
        self.extract_init_data_size   (opt_header)
        self.extract_uninit_data_size (opt_header)
        self.extract_code_base        (opt_header)
        self.extract_dll_properties   (opt_header)

    def extract_magic (self, opt_header: lief.PE.OptionalHeader) -> None:
        self.magic = opt_header.magic

    def extract_maj_link_ver (self, opt_header: lief.PE.OptionalHeader) -> None:
        self.maj_link_ver = opt_header.major_linker_version

    def extract_min_link_ver (self, opt_header: lief.PE.OptionalHeader) -> None:
        self.min_link_ver = opt_header.minor_linker_version

    def extract_code_size (self, opt_header: lief.PE.OptionalHeader) -> None:
        self.code_size = opt_header.sizeof_code
    
    def extract_init_data_size (self, opt_header: lief.PE.OptionalHeader) -> None:
        self.init_data_size = opt_header.sizeof_initialized_data

    def extract_uninit_data_size (self, opt_header: lief.PE.OptionalHeader) -> None:
        self.uninit_data_size = opt_header.sizeof_uninitialized_data

    def extract_code_base (self, opt_header: lief.PE.OptionalHeader) -> None:
        self.code_base = opt_header.baseof_code

    def extract_dll_properties (self, opt_header: lief.PE.OptionalHeader) -> None:
        self.dll_properties = opt_header.dll_characteristics


    # Accessors and mutators
    @property
    def magic (self):
        return self.__magic

    @property
    def maj_link_ver (self):
        return self.__maj_link_ver

    @property
    def min_link_ver (self):
        return self.__min_link_ver

    @property
    def code_size (self):
        return self.__code_size

    @property
    def init_data_size (self):
        return self.__init_data_size

    @property
    def unint_data_size (self):
        return self.__unint_data_size

    @property
    def code_base (self):
        return self.__code_base
    
    @property
    def dll_properties (self) -> lief.PE.DLL_CHARACTERISTICS:
        return self.__dll_properties
    
    @magic.setter
    def magic (self, m) -> None:
        self.__magic = m

    @maj_link_ver.setter
    def maj_link_ver (self, v) -> None:
        self.__maj_link_ver = v

    @min_link_ver.setter
    def min_link_ver (self, v) -> None:
        self.__min_link_ver = v

    @code_size.setter
    def code_size (self, s) -> None:
        self.__code_size = s

    @init_data_size.setter
    def init_data_size (self, s) -> None:
        self.__init_data_size = s

    @unint_data_size.setter
    def uninit_data_size (self, s) -> None:
        self.__unint_data_size = s

    @code_base.setter
    def code_base (self, b) -> None:
        self.__code_base = b

    @dll_properties.setter
    def dll_properties (self, p: lief.PE.DLL_CHARACTERISTICS) -> None:
        self.__dll_properties = p

    
    # Overloads
    def __str__ (self) -> str:
        return ("Magic: " + str( hex (self.magic)) +
                "\nLinker Version: " + str (self.maj_link_ver) + '.' + str (self.min_link_ver) +
                "\nCode Size: " + str (self.code_size) +
                "\nInit. Data Size: " + str (self.init_data_size) +
                "\nUninit. Data Size: " + str (self.uninit_data_size) +
                "\nCode Base: " + str (hex (self.code_base)) +
                "\nDLL Characts: " + str ( bin (self.dll_properties)))



if __name__ == "__main__":
    pass
