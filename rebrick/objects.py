# Created byMartin.cz
# Copyright (c) Martin Strohalm. All rights reserved.


class _Entity(object):
    """Provides a base class for all objects."""
    
    
    def __init__(self, **attrs):
        """Initializes a new instance of rebrick.Entity."""
        
        super(_Entity, self).__init__()
        
        # set given attributes
        for name, value in attrs.items():
            if hasattr(self, name):
                setattr(self, name, value)
            else:
                raise AttributeError("Attribute not found! --> %s" % name)
    
    
    def __repr__(self):
        """Gets debug string representation."""
        
        return u"%s(%s)" % (self.__class__.__name__, self.__str__())


class Category(_Entity):
    """
    Represents a Rebrickable part category definition.
    
    Attributes:
        
        category_id: int or None
            Rebrickable category ID.
            
        name: str
            Theme name.
    """
    
    
    def __init__(self, **attrs):
        """Initializes a new instance of rebrick.Category."""
        
        self.category_id = None
        self.name = None
        
        super(Category, self).__init__(**attrs)
    
    
    def __str__(self):
        """Gets standard string representation."""
        
        return u"Category ID: %s %s" % (self.category_id, self.name)
    
    
    @staticmethod
    def create(data):
        """
        Creates a new instance of rebrick.Category from given JSON data.
        
        Args:
            data: dict
                JSON data retrieved from Rebrickable.
        
        Returns:
            rebrick.Category
                Initialized category.
        """
        
        # create category
        return Category(
            category_id = data['id'],
            name = data['name'])


class Collection(_Entity):
    """
    Represents a Rebrickable set or MOC.
    
    Attributes:
        
        type: str
            Collection type as 'set' or 'moc'.
        
        collection_id: str, int or None
            Rebrickable collection ID.
        
        theme_id: int or None
            Rebrickable theme ID.
        
        name: str or None
            Collection name.
        
        year: int or None
            Set release year.
        
        pieces: int or None
            Number of pieces in collection.
        
        url: str or None
            Rebrickable page url.
        
        img_url: str or None
            Rebrickable image url.
        
        designer_name: str or None
            MOC designer name.
        
        designer_url: str or None
            Rebrickable MOC designer page url.
        
        count: int or None
            Collection quantity.
    """
    
    
    def __init__(self, **attrs):
        """Initializes a new instance of rebrick.Collection."""
        
        self.type = None
        
        self.collection_id = None
        self.theme_id = None
        self.name = None
        
        self.designer_name = None
        self.designer_url = None
        
        self.year = None
        self.pieces = None
        
        self.url = None
        self.img_url = None
        
        self.count = None
        
        super(Collection, self).__init__(**attrs)
    
    
    def __str__(self):
        """Gets standard string representation."""
        
        return u"%s ID: %s, %s" % (self.type.upper(), self.collection_id, self.name)
    
    
    @staticmethod
    def create(data, set_type="set"):
        """
        Creates a new instance of rebrick.Collection from given JSON data.
        
        Args:
            data: dict
                JSON data retrieved from Rebrickable.
            
            set_type: str
                Type of a collection to create: 'set' or 'moc'.
        
        Returns:
            rebrick.Collection
                Initialized collection.
        """
        
        # create official set
        if set_type == "set":
            return Collection(
                type = 'set',
                collection_id = data['set_num'],
                theme_id = data['theme_id'],
                name = data['name'],
                year = data['year'],
                pieces = data['num_parts'],
                url = data['set_url'],
                img_url = data['set_img_url'],
                count = data.get('quantity', None))
        
        # create MOC
        if set_type == "moc":
            return Collection(
                type = 'moc',
                collection_id = data['set_num'],
                theme_id = data['theme_id'],
                name = data['name'],
                year = data['year'],
                pieces = data['num_parts'],
                url = data['moc_url'],
                img_url = data['moc_img_url'],
                designer_name = data['designer_name'],
                designer_url = data['designer_url'])


class Color(_Entity):
    """
    Represents a Rebrickable color definition.
    
    Attributes:
        
        color_id: str or None
            Rebrickable color ID.
        
        name: str or None
            Rebrickable color name.
        
        rgb: str or None
            Red, green and blue channels defined as hex code.
        
        is_trans: bool or None
            Marks a transparent color.
         
        external_names: {str:(str,)}
            Available names for external sources.
        
        external_ids: {str:(str,)}
            Available IDs for external sources.
    """
    
    
    def __init__(self, **attrs):
        """Initializes a new instance of rebrick.Color."""
        
        self.color_id = None
        self.name = None
        self.rgb = None
        self.is_trans = None
        self.external_names = {}
        self.external_ids = {}
        
        super(Color, self).__init__(**attrs)
    
    
    def __str__(self):
        """Gets standard string representation."""
        
        return u"Color ID: %s, %s, %s" % (self.color_id, self.name, self.rgb)
    
    
    @staticmethod
    def create(data):
        """
        Creates a new instance of rebrick.Color from given JSON data.
        
        Args:
            data: dict
                JSON data retrieved from Rebrickable.
        
        Returns:
            rebrick.Color
                Initialized color.
        """
        
        # init color
        color = Color(
            color_id = data.get('id'),
            name = data['name'],
            rgb = data['rgb'])
        
        # get external names and IDs
        for name, value in data['external_ids'].items():
            color.external_names[name] = [n for l in value['ext_descrs'] for n in l]
            color.external_ids[name] = value['ext_ids']
        
        return color


class Element(_Entity):
    """
    Represents a Rebrickable element definition as a specific combination of
    part and color.
    
    Attributes:
        
        element_id: str or None
            Rebrickable element ID.
        
        design_id: str or None
            Lego design ID.
        
        part: rebrick.Part
            Part definition.
        
        color: rebrick.Color
            Color definition.
        
        img_url: str or None
            Rebrickable image url.
        
        count: int or None
            Element quantity.
        
        is_spare: bool or None
            Marks a spare element.
    """
    
    
    def __init__(self, **attrs):
        """Initializes a new instance of rebrick.Element."""
        
        self.element_id = None
        self.design_id = None
        
        self.part = None
        self.color = None
        
        self.img_url = None
        
        self.count = None
        self.is_spare = None
        
        super(Element, self).__init__(**attrs)
    
    
    def __str__(self):
        """Gets standard string representation."""
        
        return u"Element ID: %s, %s, %s" % (self.element_id, self.part, self.color)
    
    
    @staticmethod
    def create(data):
        """
        Creates a new instance of rebrick.Element from given JSON data.
        
        Args:
            data: dict
                JSON data retrieved from Rebrickable.
        
        Returns:
            rebrick.Element
                Initialized element.
        """
        
        # create part
        part = Part.create(data['part'])
        
        # create color
        color = Color.create(data['color'])
        
        # create element
        element = Element(
            part = part,
            color = color,
            element_id = data.get('element_id', None),
            design_id = data.get('design_id', None),
            img_url = data.get('element_img_url', None),
            count = data.get('quantity', None),
            is_spare = data.get('is_spare', None))
        
        return element


class Part(_Entity):
    """
    Represents a Rebrickable part definition.
    
    Attributes:
        
        part_id: str or None
            Rebrickable part ID.
        
        category_id: int or None
            Rebrickable category ID.
        
        external_ids: {str:(str,)}
            Available IDs for external sources.
        
        name: str or None
            Rebrickable part name.
        
        year_from: int or None
            Year or the first appearance.
        
        year_to: int or None
            Year or the last appearance.
        
        url: str or None
            Rebrickable page url.
        
        img_url: str or None
            Rebrickable image url.
        
        print_of: str or None
            Rebrickable ID of parent non-printed part.
        
        prints: (str,) or None
            Collection of printed versions IDs.
        
        molds: (str,) or None
            Collection of mold versions IDs.
        
        alternates: (str,) or None
            Collection of alternate versions IDs.
    """
    
    
    def __init__(self, **attrs):
        """Initializes a new instance of rebrick.Part."""
        
        self.part_id = None
        self.category_id = None
        self.external_ids = {}
        self.name = None
        
        self.year_from = None
        self.year_to = None
        
        self.url = None
        self.img_url = None
        
        self.print_of = None
        self.prints = []
        self.molds = []
        self.alternates = []
        
        super(Part, self).__init__(**attrs)
    
    
    def __str__(self):
        """Gets standard string representation."""
        
        return u"Part ID: %s, %s" % (self.part_id, self.name)
    
    
    @staticmethod
    def create(data):
        """
        Creates a new instance of rebrick.Part from given JSON data.
        
        Args:
            data: dict
                JSON data retrieved from Rebrickable.
        
        Returns:
            rebrick.Part
                Initialized part.
        """
        
        return Part(
            part_id = data['part_num'],
            category_id = data['part_cat_id'],
            external_ids = data.get('external_ids', {}),
            name = data['name'],
            year_from = data.get('year_from', None),
            year_to = data.get('year_to', None),
            url = data.get('part_url', None),
            img_url = data.get('part_img_url', None),
            print_of = data.get('print_of', None),
            prints = data.get('prints', []),
            molds = data.get('molds', []),
            alternates = data.get('alternates', []))


class Partlist(_Entity):
    """
    Represents a Rebrickable user's part list.
    
    Attributes:
        
        list_id: str, int or None
            Rebrickable part list ID.
        
        name: str or None
            Part list name.
        
        items: int or None
            Number of items in the list.
    """
    
    
    def __init__(self, **attrs):
        """Initializes a new instance of rebrick.Partlist."""
        
        self.list_id = None
        self.name = None
        self.items = None
        
        super(Partlist, self).__init__(**attrs)
    
    
    def __str__(self):
        """Gets standard string representation."""
        
        return u"ID: %s, %s (%s)" % (self.list_id, self.name, self.items)
    
    
    @staticmethod
    def create(data):
        """
        Creates a new instance of rebrick.Partlist from given JSON data.
        
        Args:
            data: dict
                JSON data retrieved from Rebrickable.
        
        Returns:
            rebrick.Partlist
                Initialized part list.
        """
        
        return Partlist(
            list_id = data['id'],
            name = data['name'],
            items = data['num_parts'])


class Setlist(_Entity):
    """
    Represents a Rebrickable user's set list.
    
    Attributes:
        
        list_id: str, int or None
            Rebrickable set list ID.
        
        name: str or None
            Set list name.
        
        items: int or None
            Number of items in the list.
    """
    
    
    def __init__(self, **attrs):
        """Initializes a new instance of rebrick.Setlist."""
        
        self.list_id = None
        self.name = None
        self.items = None
        
        super(Setlist, self).__init__(**attrs)
    
    
    def __str__(self):
        """Gets standard string representation."""
        
        return u"ID: %s, %s (%s)" % (self.list_id, self.name, self.items)
    
    
    @staticmethod
    def create(data):
        """
        Creates a new instance of rebrick.Setlist from given JSON data.
        
        Args:
            data: dict
                JSON data retrieved from Rebrickable.
        
        Returns:
            rebrick.Setlist
                Initialized set list.
        """
        
        return Setlist(
            list_id = data['id'],
            name = data['name'],
            items = data['num_sets'])


class Theme(_Entity):
    """
    Represents a Rebrickable set theme definition.
    
    Attributes:
        
        theme_id: int or None
            Rebrickable theme ID.
        
        parent_id: int or None
            Rebrickable parent theme ID.
            
        name: str
            Theme name.
    """
    
    
    def __init__(self, **attrs):
        """Initializes a new instance of rebrick.Theme."""
        
        self.theme_id = None
        self.parent_id = None
        self.name = None
        
        super(Theme, self).__init__(**attrs)
    
    
    def __str__(self):
        """Gets standard string representation."""
        
        return u"Theme ID: %s (%s) %s" % (self.theme_id, self.parent_id, self.name)
    
    
    @staticmethod
    def create(data):
        """
        Creates a new instance of rebrick.Theme from given JSON data.
        
        Args:
            data: dict
                JSON data retrieved from Rebrickable.
        
        Returns:
            rebrick.Theme
                Initialized theme.
        """
        
        # create theme
        return Theme(
            theme_id = data['id'],
            parent_id = data.get('parent_id', None),
            name = data['name'])
