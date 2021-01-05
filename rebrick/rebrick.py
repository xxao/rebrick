# Created byMartin.cz
# Copyright (c) Martin Strohalm. All rights reserved.

import json
import urllib.request
import urllib.error
from . import config
from . import api_lego as lego
from . import api_users as users
from .objects import *


class Rebrick(object):
    """Rebrick tool."""
    
    
    def __init__(self, api_key=None, user_token=None, silent=False):
        """
        Initializes a new instance of rebrick.Rebrick class.
        
        Args:
            api_key: str or None
                Rebrickable API key. If set to None, module global API key is
                used.
            
            user_token:
                Rebrickable user token. If set to None, you need to call login
                method before accessing user account functionality.
            
            silent: bool
                If set to True, all HTTP errors will be silenced and methods
                return None. If set to False, all HTTP errors are raised
                normally.
        """
        
        super().__init__()
        
        self._api_key = api_key
        self._user_token = user_token
        self._silent = silent
    
    
    def login(self, username, password):
        """
        Retrieves user login token, which is used to access user account
        functionality.
        
        Args:
            username: str
                Rebrickable login username or email.
            
            password: str
                Rebrickable login password.
        
        Returns:
            str or None
                Returns user token or None if login failed.
        """
        
        # send request
        try:
            response = users.get_token(
                username = username,
                password = password,
                api_key = self._api_key)
        
        except urllib.error.HTTPError as e:
            self._on_error(e)
            return None
        
        # get response data
        data = json.loads(response.read())
        
        # set token
        self._user_token = data.get('user_token', None)
        
        return self._user_token
    
    
    def get_categories(self):
        """
        Gets details for all available part categories.
        
        Returns:
            (rebrick.Category,) or None
                Available part categories.
        """
        
        categories = []
        page = None
        
        while True:
            
            # send request
            try:
                response = lego.get_categories(
                    page = page,
                    api_key = self._api_key)
            
            except urllib.error.HTTPError as e:
                self._on_error(e)
                return None
            
            # get response data
            data = json.loads(response.read())
            
            # create categories
            for item in data['results']:
                categories.append(Category.create(item))
            
            # check next page
            if data['next'] is None:
                break
            
            # get next page
            page = data['next']
        
        return categories
    
    
    def get_category(self, category_id):
        """
        Gets details about specific part category.
        
        Args:
            category_id: str or int
                Rebrickable category ID.
        
        Returns:
            rebrick.Category or None
                Category details.
        """
        
        # send request
        try:
            response = lego.get_category(
                category_id = category_id,
                api_key = self._api_key)
        
        except urllib.error.HTTPError as e:
            self._on_error(e)
            return None
        
        # get response data
        data = json.loads(response.read())
        
        # create category
        return Category.create(data)
    
    
    def get_colors(self):
        """
        Gets details for all available colors.
        
        Returns:
            (rebrick.Color,) or None
                Available colors.
        """
        
        colors = []
        page = None
        
        while True:
            
            # send request
            try:
                response = lego.get_colors(
                    page = page,
                    api_key = self._api_key)
            
            except urllib.error.HTTPError as e:
                self._on_error(e)
                return None
            
            # get response data
            data = json.loads(response.read())
            
            # create colors
            for item in data['results']:
                colors.append(Color.create(item))
            
            # check next page
            if data['next'] is None:
                break
            
            # get next page
            page = data['next']
        
        return colors
    
    
    def get_color(self, color_id):
        """
        Gets details about specific color.
        
        Args:
            color_id: str or int
                Rebrickable color ID.
        
        Returns:
            rebrick.Color or None
                Color details.
        """
        
        # send request
        try:
            response = lego.get_color(
                color_id = color_id,
                api_key = self._api_key)
        
        except urllib.error.HTTPError as e:
            self._on_error(e)
            return None
        
        # get response data
        data = json.loads(response.read())
        
        # create color
        return Color.create(data)
    
    
    def get_element(self, element_id):
        """
        Gets details about specific element.
        
        Args:
            element_id: str or int
                Rebrickable element ID.
        
        Returns:
            rebrick.Element or None
                Element details.
        """
        
        # send request
        try:
            response = lego.get_element(
                element_id = element_id,
                api_key = self._api_key)
        
        except urllib.error.HTTPError as e:
            self._on_error(e)
            return None
        
        # get response data
        data = json.loads(response.read())
        
        # create element
        return Element.create(data)
    
    
    def get_element_ids(self, part_id, color_id):
        """
        Gets element IDs corresponding to given part and color.
        
        Args:
            part_id: str or int
                Rebrickable part ID.
            
            color_id: str or int
                Rebrickable color ID.
        
        Returns:
            (int,) or None
                Element IDs.
        """
        
        # send request
        try:
            response = lego.get_part_color(
                part_id = part_id,
                color_id = color_id,
                api_key = self._api_key)
        
        except urllib.error.HTTPError as e:
            self._on_error(e)
            return None
        
        # get response data
        data = json.loads(response.read())
        
        # get IDs
        return data.get('elements', [])
    
    
    def get_element_image(self, element_id):
        """
        Gets image of specific element.
        
        Args:
            element_id: str or int
                Rebrickable element ID.
        
        Returns:
            bytes or None
                Image data.
        """
        
        # get image from Rebrickable
        try:
            url = config.RB_ELEMENT_IMG_URL.format(element_id)
            return self.get_file(url)
        except:
            pass
        
        # get image from LEGO
        try:
            url = config.LEGO_ELEMENT_IMG_URL.format(element_id)
            return self.get_file(url)
        except:
            pass
        
        return None
    
    
    def get_minifigs(self, search=None, set_id=None, theme_id=None, min_pieces=None, max_pieces=None):
        """
        Gets a list of all minifigs with optional filters.
        
        Args:
            search: str
                Search query.
            
            set_id: str or int
                Rebrickable set ID.
            
            theme_id: str or int
                Rebrickable theme ID.
            
            min_pieces: int
                Minimum number of parts.
            
            max_pieces: int
                Maximum number of parts.
        
        Returns:
            (rebrick.Minifig,) or None
                Available minifigs.
        """
        
        minifigs = []
        page = None
        
        while True:
            
            # send request
            try:
                response = lego.get_minifigs(
                    search = search,
                    set_id = set_id,
                    theme_id = theme_id,
                    min_pieces = min_pieces,
                    max_pieces = max_pieces,
                    page = page,
                    api_key = self._api_key)
            
            except urllib.error.HTTPError as e:
                self._on_error(e)
                return None
            
            # get response data
            data = json.loads(response.read())
            
            # create minifigs
            for item in data['results']:
                minifigs.append(Minifig.create(item))
            
            # check next page
            if data['next'] is None:
                break
            
            # get next page
            page = data['next']
        
        return minifigs
    
    
    def get_minifig(self, minifig_id):
        """
        Gets details about specific minifig.
        
        Args:
            minifig_id: str
                Rebrickable minifig ID.
        
        Returns:
            rebrick.Minifig or None
                Minifig details.
        """
        
        # send request
        try:
            response = lego.get_minifig(
                minifig_id = minifig_id,
                api_key = self._api_key)
        
        except urllib.error.HTTPError as e:
            self._on_error(e)
            return None
        
        # get response data
        data = json.loads(response.read())
        
        # create minifig
        return Minifig.create(data)
    
    
    def get_minifig_elements(self, minifig_id, part_details=False):
        """
        Gets list of elements for a specific minifig.
        
        Args:
            minifig_id: str
                Rebrickable minifig ID.
            
            part_details: bool
                If set to True part details will be retrieved.
        
        Returns:
            (rebrick.Element,) or None
                Minifig elements.
        """
        
        elements = []
        page = None
        
        while True:
            
            # send request
            try:
                response = lego.get_minifig_elements(
                    minifig_id = minifig_id,
                    part_details = part_details,
                    page = page,
                    api_key = self._api_key)
            
            except urllib.error.HTTPError as e:
                self._on_error(e)
                return None
            
            # get response data
            data = json.loads(response.read())
            
            # create elements
            for item in data['results']:
                elements.append(Element.create(item))
            
            # check next page
            if data['next'] is None:
                break
            
            # get next page
            page = data['next']
        
        return elements
    
    
    def get_minifig_sets(self, minifig_id):
        """
        Gets details about available sets containing specific minifig.
        
        Args:
            minifig_id: str
                Rebrickable minifig ID.
            
        Returns:
            (rebrick.Collection,) or None
                Minifig sets.
        """
        
        sets = []
        page = None
        
        while True:
            
            # send request
            try:
                response = lego.get_minifig_sets(
                    minifig_id = minifig_id,
                    page = page,
                    api_key = self._api_key)
            
            except urllib.error.HTTPError as e:
                self._on_error(e)
                return None
            
            # get response data
            data = json.loads(response.read())
            
            # get sets
            for item in data['results']:
                sets.append(Collection.create(item, COLL_SET))
            
            # check next page
            if data['next'] is None:
                break
            
            # get next page
            page = data['next']
        
        return sets
    
    
    def get_moc(self, moc_id):
        """
        Gets details about specific MOC.
        
        Args:
            moc_id: str or int
                Rebrickable MOC ID.
        
        Returns:
            rebrick.Collection or None
                MOC details.
        """
        
        # send request
        try:
            response = lego.get_moc(
                moc_id = moc_id,
                api_key = self._api_key)
        
        except urllib.error.HTTPError as e:
            self._on_error(e)
            return None
        
        # get response data
        data = json.loads(response.read())
        
        # create set
        return Collection.create(data, COLL_MOC)
    
    
    def get_moc_elements(self, moc_id, part_details=False):
        """
        Gets list of elements for a specific MOC.
        
        Args:
            moc_id: str or int
                Rebrickable MOC ID.
            
            part_details: bool
                If set to True part details will be retrieved.
        
        Returns:
            (rebrick.Element,) or None
                MOC elements.
        """
        
        elements = []
        page = None
        
        while True:
            
            # send request
            try:
                response = lego.get_moc_elements(
                    moc_id = moc_id,
                    part_details = part_details,
                    page = page,
                    api_key = self._api_key)
            
            except urllib.error.HTTPError as e:
                self._on_error(e)
                return None
            
            # get response data
            data = json.loads(response.read())
            
            # create elements
            for item in data['results']:
                elements.append(Element.create(item))
            
            # check next page
            if data['next'] is None:
                break
            
            # get next page
            page = data['next']
        
        return elements
    
    
    def get_parts(self, search=None, part_id=None, part_ids=None, part_cat_id=None, color_id=None, bricklink_id=None, brickowl_id=None, lego_id=None, ldraw_id=None, part_details=False):
        """
        Gets details for all available parts with optional filters.
        
        Args:
            search: str
                Search query.
            
            part_id: str or int
                Rebrickable part ID.
            
            part_ids: (str,), (int,) or None
                Rebrickable part IDs.
            
            part_cat_id: str or int
                Rebrickable part category ID.
            
            color_id: str or int
                Rebrickable color ID.
            
            bricklink_id: str or int
                Bricklink part ID.
            
            brickowl_id: str or int
                BrickOwl part ID.
            
            lego_id: str or int
                LEGO part ID.
            
            ldraw_id: str or int
                LDraw part ID.
            
            part_details: bool
                If set to True part details will be retrieved.
        
        Returns:
            (rebrick.Part,) or None
                Available parts.
        """
        
        parts = []
        page = None
        
        while True:
            
            # send request
            try:
                response = lego.get_parts(
                    search = search,
                    part_id = part_id,
                    part_ids = part_ids,
                    part_cat_id = part_cat_id,
                    color_id = color_id,
                    bricklink_id = bricklink_id,
                    brickowl_id = brickowl_id,
                    lego_id = lego_id,
                    ldraw_id = ldraw_id,
                    part_details = part_details,
                    page = page,
                    api_key = self._api_key)
            
            except urllib.error.HTTPError as e:
                self._on_error(e)
                return None
            
            # get response data
            data = json.loads(response.read())
            
            # create parts
            for item in data['results']:
                parts.append(Part.create(item))
            
            # check next page
            if data['next'] is None:
                break
            
            # get next page
            page = data['next']
        
        return parts
    
    
    def get_part(self, part_id):
        """
        Gets details about specific part.
        
        Args:
            part_id: str or int
                Rebrickable part ID.
        
        Returns:
            rebrick.Part or None
                Part details.
        """
        
        # send request
        try:
            response = lego.get_part(
                part_id = part_id,
                api_key = self._api_key)
        
        except urllib.error.HTTPError as e:
            self._on_error(e)
            return None
        
        # get response data
        data = json.loads(response.read())
        
        # create part
        return Part.create(data)
    
    
    def get_part_colors(self, part_id):
        """
        Gets details about available colors for specific part.
        
        Args:
            part_id: str or int
                Rebrickable part ID.
        
        Returns:
            (rebrick.Color,) or None
                Part colors.
        """
        
        colors = []
        page = None
        
        # get all colors
        lookup = {c.color_id: c for c in self.get_colors()}
        
        while True:
            
            # send request
            try:
                response = lego.get_part_colors(
                    part_id = part_id,
                    page = page,
                    api_key = self._api_key)
            
            except urllib.error.HTTPError as e:
                self._on_error(e)
                return None
            
            # get response data
            data = json.loads(response.read())
            
            # get colors
            for item in data['results']:
                if item['color_id'] in lookup:
                    colors.append(lookup[item['color_id']])
            
            # check next page
            if data['next'] is None:
                break
            
            # get next page
            page = data['next']
        
        return colors
    
    
    def get_part_color_sets(self, part_id, color_id):
        """
        Gets details about available sets containing specific part/color
        combination.
        
        Args:
            part_id: str or int
                Rebrickable part ID.
            
            color_id: str or int
                Rebrickable color ID.
            
        Returns:
            (rebrick.Collection,) or None
                Part color sets.
        """
        
        sets = []
        page = None
        
        while True:
            
            # send request
            try:
                response = lego.get_part_color_sets(
                    part_id = part_id,
                    color_id = color_id,
                    page = page,
                    api_key = self._api_key)
            
            except urllib.error.HTTPError as e:
                self._on_error(e)
                return None
            
            # get response data
            data = json.loads(response.read())
            
            # get sets
            for item in data['results']:
                sets.append(Collection.create(item, COLL_SET))
            
            # check next page
            if data['next'] is None:
                break
            
            # get next page
            page = data['next']
        
        return sets
    
    
    def get_sets(self, search=None, theme_id=None, min_year=None, max_year=None, min_pieces=None, max_pieces=None):
        """
        Gets a list of all sets with optional filters.
        
        Args:
            search: str
                Search query.
            
            theme_id: str or int
                Rebrickable theme ID.
            
            min_year: int
                Minimum release year.
            
            max_year: int
                Maximum release year.
            
            min_pieces: int
                Minimum number of parts.
            
            max_pieces: int
                Maximum number of parts.
        
        Returns:
            (rebrick.Collection,) or None
                Available sets.
        """
        
        sets = []
        page = None
        
        while True:
            
            # send request
            try:
                response = lego.get_sets(
                    search = search,
                    theme_id = theme_id,
                    min_year = min_year,
                    max_year = max_year,
                    min_pieces = min_pieces,
                    max_pieces = max_pieces,
                    page = page,
                    api_key = self._api_key)
            
            except urllib.error.HTTPError as e:
                self._on_error(e)
                return None
            
            # get response data
            data = json.loads(response.read())
            
            # create collections
            for item in data['results']:
                sets.append(Collection.create(item, COLL_SET))
            
            # check next page
            if data['next'] is None:
                break
            
            # get next page
            page = data['next']
        
        return sets
    
    
    def get_set(self, set_id):
        """
        Gets details about specific set.
        
        Args:
            set_id: str or int
                Rebrickable set ID.
        
        Returns:
            rebrick.Collection or None
                Set details.
        """
        
        # send request
        try:
            response = lego.get_set(
                set_id = set_id,
                api_key = self._api_key)
        
        except urllib.error.HTTPError as e:
            self._on_error(e)
            return None
        
        # get response data
        data = json.loads(response.read())
        
        # create set
        return Collection.create(data, COLL_SET)
    
    
    def get_set_alternates(self, set_id):
        """
        Gets details about available alternate builds for specific set.
        
        Args:
            set_id: str or int
                Rebrickable set ID.
        
        Returns:
            (rebrick.Collection,) or None
                Alternate sets.
        """
        
        sets = []
        page = None
        
        while True:
            
            # send request
            try:
                response = lego.get_set_alternates(
                    set_id = set_id,
                    page = page,
                    api_key = self._api_key)
            
            except urllib.error.HTTPError as e:
                self._on_error(e)
                return None
            
            # get response data
            data = json.loads(response.read())
            
            # create elements
            for item in data['results']:
                sets.append(Collection.create(item, COLL_MOC))
            
            # check next page
            if data['next'] is None:
                break
            
            # get next page
            page = data['next']
        
        return sets
    
    
    def get_set_elements(self, set_id, part_details=False, color_details=True, minifig_parts=False):
        """
        Gets list of elements for a specific set.
        
        Args:
            set_id: str or int
                Rebrickable set ID.
            
            part_details: bool
                If set to True part details will be retrieved.
            
            color_details: bool
                If set to True color details will be retrieved.
            
            minifig_parts: bool
                If set to True, minifig parts wil be retrieved.
        
        Returns:
            (rebrick.Element,) or None
                Set elements.
        """
        
        elements = []
        page = None
        
        while True:
            
            # send request
            try:
                response = lego.get_set_elements(
                    set_id = set_id,
                    part_details = part_details,
                    color_details = color_details,
                    minifig_parts = minifig_parts,
                    page = page,
                    api_key = self._api_key)
            
            except urllib.error.HTTPError as e:
                self._on_error(e)
                return None
            
            # get response data
            data = json.loads(response.read())
            
            # create elements
            for item in data['results']:
                elements.append(Element.create(item))
            
            # check next page
            if data['next'] is None:
                break
            
            # get next page
            page = data['next']
        
        return elements
    
    
    def get_set_minifigs(self, set_id):
        """
        Gets details about available minifigs for specific set.
        
        Args:
            set_id: str or int
                Rebrickable set ID.
        
        Returns:
            (rebrick.Minifig,) or None
                Set minifigs.
        """
        
        minifigs = []
        page = None
        
        while True:
            
            # send request
            try:
                response = lego.get_set_minifigs(
                    set_id = set_id,
                    page = page,
                    api_key = self._api_key)
            
            except urllib.error.HTTPError as e:
                self._on_error(e)
                return None
            
            # get response data
            data = json.loads(response.read())
            
            # create minifigs
            for item in data['results']:
                minifigs.append(Minifig.create(item))
            
            # check next page
            if data['next'] is None:
                break
            
            # get next page
            page = data['next']
        
        return minifigs
    
    
    def get_set_themes(self, set_id):
        """
        Gets hierarchy of themes for a specific set.
        
        Args:
            set_id: str or int
                Rebrickable set ID.
        
        Returns:
            (rebrick.Theme,) or None
                Set theme hierarchy.
        """
        
        themes = []
        
        # send request
        try:
            response = lego.get_set(
                set_id = set_id,
                api_key = self._api_key)
        
        except urllib.error.HTTPError as e:
            self._on_error(e)
            return None
        
        # get response data
        data = json.loads(response.read())
        
        # get theme ID
        theme_id = data['theme_id']
        
        # retrieve theme hierarchy
        while theme_id:
            
            # send request
            try:
                response = lego.get_theme(
                    theme_id = theme_id,
                    api_key = self._api_key)
            
            except urllib.error.HTTPError as e:
                self._on_error(e)
                return None
            
            # get response data
            data = json.loads(response.read())
            
            # create theme
            theme = Theme.create(data)
            themes.insert(0, theme)
            
            # get parent ID
            theme_id = theme.parent_id
        
        return themes
    
    
    def get_set_image(self, set_id):
        """
        Gets image of specific set.

        Args:
            set_id: str
                Rebrickable set ID.

        Returns:
            bytes or None
                Image data.
        """
        
        if '-' not in str(set_id):
            set_id = "%s-1" % set_id
        
        url = config.SET_IMG_URL.format(set_id)
        
        try:
            return self.get_file(url)
        except:
            return None
    
    
    def get_themes(self):
        """
        Gets details for all available themes.
        
        Returns:
            (rebrick.Theme,) or None
                Available colors.
        """
        
        themes = []
        page = None
        
        while True:
            
            # send request
            try:
                response = lego.get_themes(
                    page = page,
                    api_key = self._api_key)
            
            except urllib.error.HTTPError as e:
                self._on_error(e)
                return None
            
            # get response data
            data = json.loads(response.read())
            
            # create themes
            for item in data['results']:
                themes.append(Theme.create(item))
            
            # check next page
            if data['next'] is None:
                break
            
            # get next page
            page = data['next']
        
        return themes
    
    
    def get_theme(self, theme_id):
        """
        Gets details about specific theme.
        
        Args:
            theme_id: str or int
                Rebrickable theme ID.
        
        Returns:
            rebrick.Theme or None
                Theme details.
        """
        
        # send request
        try:
            response = lego.get_theme(
                theme_id = theme_id,
                api_key = self._api_key)
        
        except urllib.error.HTTPError as e:
            self._on_error(e)
            return None
        
        # get response data
        data = json.loads(response.read())
        
        # create theme
        return Theme.create(data)
    
    
    def get_users_elements(self, part_id=None, part_cat_id=None, color_id=None, part_details=False):
        """
        Gets details for all user's elements in part lists and own sets with
        optional filters.
        
        Args:
            part_id: str, int or None
                Rebrickable part ID.
            
            part_cat_id: str, int or None
                Rebrickable category ID.
            
            color_id: str, int or None
                Rebrickable color ID.
            
            part_details: bool
                If set to True part details will be retrieved.
        
        Returns:
            (rebrick.Element,) or None
                Lost elements.
        """
        
        elements = []
        page = None
        
        while True:
            
            # send request
            try:
                response = users.get_elements(
                    part_id = part_id,
                    part_cat_id = part_cat_id,
                    color_id = color_id,
                    part_details = part_details,
                    page = page,
                    user_token = self._user_token,
                    api_key = self._api_key)
            
            except urllib.error.HTTPError as e:
                self._on_error(e)
                return None
            
            # get response data
            data = json.loads(response.read())
            
            # get results
            for item in data['results']:
                elements.append(Element.create(item))
            
            # check next page
            if data['next'] is None:
                break
            
            # get next page
            page = data['next']
        
        return elements
    
    
    def get_users_lost_elements(self, part_details=False):
        """
        Gets details for all user's lost elements.
        
        Args:
            part_details: bool
                If set to True part details will be retrieved.
        
        Returns:
            (rebrick.Element,) or None
                Lost elements.
        """
        
        elements = []
        page = None
        
        while True:
            
            # send request
            try:
                response = users.get_lost_elements(
                    part_details = part_details,
                    page = page,
                    user_token = self._user_token,
                    api_key = self._api_key)
            
            except urllib.error.HTTPError as e:
                self._on_error(e)
                return None
            
            # get response data
            data = json.loads(response.read())
            
            # get results
            for item in data['results']:
                elements.append(Element.create(item))
            
            # check next page
            if data['next'] is None:
                break
            
            # get next page
            page = data['next']
        
        return elements
    
    
    def get_users_partlists(self):
        """
        Gets a list of all user's part lists.
        
        Returns:
            (rebrick.Partlist,)
                Available part lists.
        """
        
        partlists = []
        page = None
        
        while True:
            
            # send request
            try:
                response = users.get_partlists(
                    page = page,
                    user_token = self._user_token,
                    api_key = self._api_key)
            
            except urllib.error.HTTPError as e:
                self._on_error(e)
                return None
            
            # get response data
            data = json.loads(response.read())
            
            # create partlists
            for item in data['results']:
                partlists.append(Partlist.create(item))
            
            # check next page
            if data['next'] is None:
                break
            
            # get next page
            page = data['next']
        
        return partlists
    
    
    def get_users_partlist(self, list_id):
        """
        Gets details about specific user's parts list.
        
        Args:
            list_id: str or int
                Rebrickable part list ID.
        
        Returns:
            rebrick.Partlist or None
                Part list details.
        """
        
        # send request
        try:
            response = users.get_partlist(
                list_id = list_id,
                user_token = self._user_token,
                api_key = self._api_key)
        
        except urllib.error.HTTPError as e:
            self._on_error(e)
            return None
        
        # get response data
        data = json.loads(response.read())
        
        # create partlist
        return Partlist.create(data)
    
    
    def get_users_partlist_elements(self, list_id, part_details=False):
        """
        Gets list of elements for specific user's parts list.
        
        Args:
            list_id: str or int
                Rebrickable part list ID.
            
            part_details: bool
                If set to True part details will be retrieved.
            
        Returns:
            (rebrick.Element,) or None
                Part list elements.
        """
        
        elements = []
        page = None
        
        while True:
            
            # send request
            try:
                response = users.get_partlist_elements(
                    list_id = list_id,
                    part_details = part_details,
                    page = page,
                    user_token = self._user_token,
                    api_key = self._api_key)
            
            except urllib.error.HTTPError as e:
                self._on_error(e)
                return None
            
            # get response data
            data = json.loads(response.read())
            
            # get results
            for item in data['results']:
                elements.append(Element.create(item))
            
            # check next page
            if data['next'] is None:
                break
            
            # get next page
            page = data['next']
        
        return elements
    
    
    def get_users_sets(self, search=None, theme_id=None, min_year=None, max_year=None, min_pieces=None, max_pieces=None):
        """
        Gets details for all user's own sets with optional filters.
        
        Args:
            search: str
                Search query.
            
            theme_id: str or int
                Rebrickable theme ID.
            
            min_year: int
                Minimum release year.
            
            max_year: int
                Maximum release year.
            
            min_pieces: int
                Minimum number of parts.
            
            max_pieces: int
                Maximum number of parts.
        
        Returns:
            (rebrick.Collection,) or None
                Available sets.
        """
        
        sets = []
        page = None
        
        while True:
            
            # send request
            try:
                response = users.get_sets(
                    search = search,
                    theme_id = theme_id,
                    min_year = min_year,
                    max_year = max_year,
                    min_pieces = min_pieces,
                    max_pieces = max_pieces,
                    page = page,
                    user_token = self._user_token,
                    api_key = self._api_key)
            
            except urllib.error.HTTPError as e:
                self._on_error(e)
                return None
            
            # get response data
            data = json.loads(response.read())
            
            # create collections
            for item in data['results']:
                item['set']['quantity'] = item['quantity']
                sets.append(Collection.create(item['set'], COLL_SET))
            
            # check next page
            if data['next'] is None:
                break
            
            # get next page
            page = data['next']
        
        return sets
    
    
    def get_users_setlists(self):
        """
        Gets a list of all user's set lists.
        
        Returns:
            (rebrick.Setlist,)
                Available set lists.
        """
        
        setlists = []
        page = None
        
        while True:
            
            # send request
            try:
                response = users.get_setlists(
                    page = page,
                    user_token = self._user_token,
                    api_key = self._api_key)
            
            except urllib.error.HTTPError as e:
                self._on_error(e)
                return None
            
            # get response data
            data = json.loads(response.read())
            
            # create setlists
            for item in data['results']:
                setlists.append(Setlist.create(item))
            
            # check next page
            if data['next'] is None:
                break
            
            # get next page
            page = data['next']
        
        return setlists
    
    
    def get_users_setlist(self, list_id):
        """
        Gets details about specific user's set list.
        
        Args:
            list_id: str or int
                Rebrickable set list ID.
        
        Returns:
            rebrick.Setlist or None
                Set list details.
        """
        
        # send request
        try:
            response = users.get_setlist(
                list_id = list_id,
                user_token = self._user_token,
                api_key = self._api_key)
        
        except urllib.error.HTTPError as e:
            self._on_error(e)
            return None
        
        # get response data
        data = json.loads(response.read())
        
        # create setlist
        return Setlist.create(data)
    
    
    def get_users_setlist_sets(self, list_id):
        """
        Gets a list of all user's sets within specific set list.
        
        Args:
            list_id: str or int
                Rebrickable set list ID.
        
        Returns:
            (rebrick.Collection,) or None
                Available sets.
        """
        
        sets = []
        page = None
        
        while True:
            
            # send request
            try:
                response = users.get_setlist_sets(
                    list_id = list_id,
                    page = page,
                    user_token = self._user_token,
                    api_key = self._api_key)
            
            except urllib.error.HTTPError as e:
                self._on_error(e)
                return None
            
            # get response data
            data = json.loads(response.read())
            
            # create collections
            for item in data['results']:
                item['set']['quantity'] = item['quantity']
                sets.append(Collection.create(item['set'], COLL_SET))
            
            # check next page
            if data['next'] is None:
                break
            
            # get next page
            page = data['next']
        
        return sets
    
    
    def get_file(self, url):
        """
        Downloads a file from given URL.
        
        Args:
            url: str
                URL of the file to download.
        
        Returns:
            bytes
                File data.
        """
        
        # make request
        request = urllib.request.Request(url, headers={'User-Agent': 'Rebrick Tool'})
        
        # send request
        try:
            response = urllib.request.urlopen(request)
        
        except urllib.error.HTTPError as e:
            self._on_error(e)
            return None
        
        # get response data
        return response.read()
    
    
    def _on_error(self, error):
        """Process request error."""
        
        if self._silent:
            return
        
        raise error
