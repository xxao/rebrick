# Created byMartin.cz
# Copyright (c) Martin Strohalm. All rights reserved.

# See the Rebrickable API documentation at https://rebrickable.com/api/v3/docs/

from . import config
from .request import request


def get_categories(page=None, page_size=None, ordering=None, api_key=None):
    """
    Gets details for all available part categories.
    
    Args:
        page: int or None
            A page number within the paginated result set.
        
        page_size: int or None
            Number of results to return per page.
        
        ordering: str or None
            Specifies the field to use for results ordering.
        
        api_key: str or None
            Rebrickable API access key. If set to None the one set by
            rebrick.init() is used.
    
    Returns:
        http.client.HTTPResponse
            Server response.
    """
    
    parameters = {
        'page': page,
        'page_size': page_size,
        'ordering': ordering,
        'key': api_key}
    
    path = config.API_LEGO_URL + "part_categories/"
    
    return request(path, parameters)


def get_category(category_id, api_key=None):
    """
    Gets details about specific part category.
    
    Args:
        category_id: str or int
            Rebrickable category ID.
        
        api_key: str or None
            Rebrickable API access key. If set to None the one set by
            rebrick.init() is used.
    
    Returns:
        http.client.HTTPResponse
            Server response.
    """
    
    parameters = {'key': api_key}
    
    path = config.API_LEGO_URL + "part_categories/%s/" % category_id
    
    return request(path, parameters)


def get_colors(page=None, page_size=None, ordering=None, api_key=None):
    """
    Gets details for all available colors.
    
    Args:
        page: int or None
            A page number within the paginated result set.
        
        page_size: int or None
            Number of results to return per page.
        
        ordering: str or None
            Specifies the field to use for results ordering.
        
        api_key: str or None
            Rebrickable API access key. If set to None the one set by
            rebrick.init() is used.
    
    Returns:
        http.client.HTTPResponse
            Server response.
    """
    
    parameters = {
        'page': page,
        'page_size': page_size,
        'ordering': ordering,
        'key': api_key}
    
    path = config.API_LEGO_URL + "colors/"
    
    return request(path, parameters)


def get_color(color_id, api_key=None):
    """
    Gets details about specific color.
    
    Args:
        color_id: str or int
            Rebrickable color ID.
        
        api_key: str or None
            Rebrickable API access key. If set to None the one set by
            rebrick.init() is used.
    
    Returns:
        http.client.HTTPResponse
            Server response.
    """
    
    parameters = {'key': api_key}
    
    path = config.API_LEGO_URL + "colors/%s/" % color_id
    
    return request(path, parameters)


def get_element(element_id, api_key=None):
    """
    Gets details about specific element.
    
    Args:
        element_id: str or int
            Rebrickable element ID.
        
        api_key: str or None
            Rebrickable API access key. If set to None the one set by
            rebrick.init() is used.
    
    Returns:
        http.client.HTTPResponse
            Server response.
    """
    
    parameters = {'key': api_key}
    
    path = config.API_LEGO_URL + "elements/%s/" % element_id
    
    return request(path, parameters)


def get_minifigs(search=None, set_id=None, theme_id=None, min_pieces=None, max_pieces=None, page=None, page_size=None, ordering=None, api_key=None):
    """
    Gets details for all available minifigs with optional filters.
    
    Args:
        search: str, int or None
            Search term e.g. minifig ID or name.
        
        set_id: str, int or None
            Rebrickable set ID.
        
        theme_id: str, int or None
            Rebrickable theme ID.
        
        min_pieces: int or None
            Minimum number of pieces.
        
        max_pieces: int or None
            Maximum number of pieces.
        
        page: int or None
            A page number within the paginated result set.
        
        page_size: int or None
            Number of results to return per page.
        
        ordering: str or None
            Specifies the field to use for results ordering.
        
        api_key: str or None
            Rebrickable API access key. If set to None the one set by
            rebrick.init() is used.
    
    Returns:
        http.client.HTTPResponse
            Server response.
    """
    
    parameters = {
        'search': search,
        'in_set_num': set_id,
        'in_theme_id': theme_id,
        'min_parts': min_pieces,
        'max_parts': max_pieces,
        'page': page,
        'page_size': page_size,
        'ordering': ordering,
        'key': api_key}
    
    path = config.API_LEGO_URL + "minifigs/"
    
    return request(path, parameters)


def get_minifig(minifig_id, api_key=None):
    """
    Gets details about specific minifig.
    
    Args:
        minifig_id: str or int
            Rebrickable minifig ID.
        
        api_key: str or None
            Rebrickable API access key. If set to None the one set by
            rebrick.init() is used.
    
    Returns:
        http.client.HTTPResponse
            Server response.
    """
    
    parameters = {'key': api_key}
    
    path = config.API_LEGO_URL + "minifigs/%s/" % minifig_id
    
    return request(path, parameters)


def get_minifig_elements(minifig_id, part_details=False, color_details=True, page=None, page_size=None, ordering=None, api_key=None):
    """
    Gets details about available elements for specific minifig.
    
    Args:
        minifig_id: str or int
            Rebrickable minifig ID.
        
        part_details: bool
            If set to True part details will be retrieved.
        
        color_details: bool
            If set to True color details will be retrieved.
        
        page: int or None
            A page number within the paginated result set.
        
        page_size: int or None
            Number of results to return per page.
        
        ordering: str or None
            Specifies the field to use for results ordering.
        
        api_key: str or None
            Rebrickable API access key. If set to None the one set by
            rebrick.init() is used.
    
    Returns:
        http.client.HTTPResponse
            Server response.
    """
    
    parameters = {
        'inc_part_details': int(part_details),
        'inc_color_details': int(color_details),
        'page': page,
        'page_size': page_size,
        'ordering': ordering,
        'key': api_key}
    
    path = config.API_LEGO_URL + "minifigs/%s/parts/" % minifig_id
    
    return request(path, parameters)


def get_minifig_sets(minifig_id, page=None, page_size=None, ordering=None, api_key=None):
    """
    Gets details about available sets containing specific minifig.
    
    Args:
        minifig_id: str or int
            Rebrickable minifig ID.
        
        page: int or None
            A page number within the paginated result set.
        
        page_size: int or None
            Number of results to return per page.
        
        ordering: str or None
            Specifies the field to use for results ordering.
        
        api_key: str or None
            Rebrickable API access key. If set to None the one set by
            rebrick.init() is used.
    
    Returns:
        http.client.HTTPResponse
            Server response.
    """
    
    parameters = {
        'page': page,
        'page_size': page_size,
        'ordering': ordering,
        'key': api_key}
    
    path = config.API_LEGO_URL + "minifigs/%s/sets/" % minifig_id
    
    return request(path, parameters)


def get_moc(moc_id, api_key=None):
    """
    Gets details about specific MOC. This is no longer supported by API!
    
    Args:
        moc_id: str or int
            Rebrickable MOC ID.
        
        api_key: str or None
            Rebrickable API access key. If set to None the one set by
            rebrick.init() is used.
    
    Returns:
        http.client.HTTPResponse
            Server response.
    """
    
    # no longer supported
    raise NotImplementedError("MOCs are no longer available via API.")
    
    if 'MOC' not in str(moc_id):
        moc_id = "MOC-%s" % moc_id
    
    parameters = {'key': api_key}
    
    path = config.API_LEGO_URL + "mocs/%s/" % moc_id
    
    return request(path, parameters)


def get_moc_elements(moc_id, part_details=False, page=None, page_size=None, ordering=None, api_key=None):
    """
    Gets list of elements for a specific MOC. This is no longer supported by API!
    
    Args:
        moc_id: str or int
            Rebrickable MOC ID.
        
        part_details: bool
            If set to True part details will be retrieved.
        
        page: int or None
            A page number within the paginated result set.
        
        page_size: int or None
            Number of results to return per page.
        
        ordering: str or None
            Specifies the field to use for results ordering.
        
        api_key: str or None
            Rebrickable API access key. If set to None the one set by
            rebrick.init() is used.
    
    Returns:
        http.client.HTTPResponse
            Server response.
    """
    
    # no longer supported
    raise NotImplementedError("MOCs are no longer available via API.")
    
    if 'MOC' not in str(moc_id):
        moc_id = "MOC-%s" % moc_id
    
    parameters = {
        'inc_part_details': int(part_details),
        'page': page,
        'page_size': page_size,
        'ordering': ordering,
        'key': api_key}
    
    path = config.API_LEGO_URL + "mocs/%s/parts/" % moc_id
    
    return request(path, parameters)


def get_parts(search=None, part_id=None, part_ids=None, part_cat_id=None, color_id=None, bricklink_id=None, brickowl_id=None, lego_id=None, ldraw_id=None, part_details=False, page=None, page_size=None, ordering=None, api_key=None):
    """
    Gets details for all available parts with optional filters.
    
    Args:
        search: str, int or None
            Search term e.g. part ID or name.
        
        part_id: str, int or None
            Rebrickable part ID.
        
        part_ids: (str,), (int,) or None
            Rebrickable part IDs.
        
        part_cat_id: str, int or None
            Rebrickable category ID.
        
        color_id: str, int or None
            Rebrickable color ID.
        
        bricklink_id: str, int or None
            BrickLink part ID.
        
        brickowl_id: str, int or None
            BrickOwl part ID.
        
        lego_id: str, int or None
            LEGO part ID.
        
        ldraw_id: str, int or None
            LDraw part ID.
        
        part_details: bool
            If set to True part details will be retrieved.
        
        page: int or None
            A page number within the paginated result set.
        
        page_size: int or None
            Number of results to return per page.
        
        ordering: str or None
            Specifies the field to use for results ordering.
        
        api_key: str or None
            Rebrickable API access key. If set to None the one set by
            rebrick.init() is used.
    
    Returns:
        http.client.HTTPResponse
            Server response.
    """
    
    if part_ids and not isinstance(part_id, str):
        part_ids = ",".join(str(i) for i in part_ids)
    
    parameters = {
        'search': search,
        'part_num': part_id,
        'part_nums': part_ids,
        'part_cat_id': part_cat_id,
        'color_id': color_id,
        'bricklink_id': bricklink_id,
        'brickowl_id': brickowl_id,
        'lego_id': lego_id,
        'ldraw_id': ldraw_id,
        'inc_part_details': int(part_details),
        'page': page,
        'page_size': page_size,
        'ordering': ordering,
        'key': api_key}
    
    path = config.API_LEGO_URL + "parts/"
    
    return request(path, parameters)


def get_part(part_id, api_key=None):
    """
    Gets details about specific part.
    
    Args:
        part_id: str or int
            Rebrickable part ID.
        
        api_key: str or None
            Rebrickable API access key. If set to None the one set by
            rebrick.init() is used.
    
    Returns:
        http.client.HTTPResponse
            Server response.
    """
    
    parameters = {'key': api_key}
    
    path = config.API_LEGO_URL + "parts/%s/" % part_id
    
    return request(path, parameters)


def get_part_color(part_id, color_id, api_key=None):
    """
    Gets details about specific part/color combination.
    
    Args:
        part_id: str or int
            Rebrickable part ID.
        
        color_id: str or int
            Rebrickable color ID.
        
        api_key: str or None
            Rebrickable API access key. If set to None the one set by
            rebrick.init() is used.
    
    Returns:
        http.client.HTTPResponse
            Server response.
    """
    
    parameters = {'key': api_key}
    
    path = config.API_LEGO_URL + "parts/%s/colors/%s/" % (part_id, color_id)
    
    return request(path, parameters)


def get_part_colors(part_id, page=None, page_size=None, ordering=None, api_key=None):
    """
    Gets details about available colors for specific part.
    
    Args:
        part_id: str or int
            Rebrickable part ID.
        
        page: int or None
            A page number within the paginated result set.
        
        page_size: int or None
            Number of results to return per page.
        
        ordering: str or None
            Specifies the field to use for results ordering.
        
        api_key: str or None
            Rebrickable API access key. If set to None the one set by
            rebrick.init() is used.
    
    Returns:
        http.client.HTTPResponse
            Server response.
    """
    
    parameters = {
        'page': page,
        'page_size': page_size,
        'ordering': ordering,
        'key': api_key}
    
    path = config.API_LEGO_URL + "parts/%s/colors/" % part_id
    
    return request(path, parameters)


def get_part_color_sets(part_id, color_id, page=None, page_size=None, ordering=None, api_key=None):
    """
    Gets details about available sets containing specific part/color
    combination.
    
    Args:
        part_id: str or int
            Rebrickable part ID.
        
        color_id: str or int
            Rebrickable color ID.
        
        page: int or None
            A page number within the paginated result set.
        
        page_size: int or None
            Number of results to return per page.
        
        ordering: str or None
            Specifies the field to use for results ordering.
        
        api_key: str or None
            Rebrickable API access key. If set to None the one set by
            rebrick.init() is used.
    
    Returns:
        http.client.HTTPResponse
            Server response.
    """
    
    parameters = {
        'page': page,
        'page_size': page_size,
        'ordering': ordering,
        'key': api_key}
    
    path = config.API_LEGO_URL + "parts/%s/colors/%s/sets/" % (part_id, color_id)
    
    return request(path, parameters)


def get_sets(search=None, theme_id=None, min_year=None, max_year=None, min_pieces=None, max_pieces=None, page=None, page_size=None, ordering=None, api_key=None):
    """
    Gets details for all available sets with optional filters.
    
    Args:
        search: str, int or None
            Search term e.g. set ID or name.
        
        theme_id: str, int or None
            Rebrickable theme ID.
        
        min_year: int or None
            Minimum allowed release year.
        
        max_year: int or None
            Maximum allowed release year.
        
        min_pieces: int or None
            Minimum number of pieces.
        
        max_pieces: int or None
            Maximum number of pieces.
        
        page: int or None
            A page number within the paginated result set.
        
        page_size: int or None
            Number of results to return per page.
        
        ordering: str or None
            Specifies the field to use for results ordering.
        
        api_key: str or None
            Rebrickable API access key. If set to None the one set by
            rebrick.init() is used.
    
    Returns:
        http.client.HTTPResponse
            Server response.
    """
    
    parameters = {
        'search': search,
        'theme_id': theme_id,
        'min_year': min_year,
        'max_year': max_year,
        'min_parts': min_pieces,
        'max_parts': max_pieces,
        'page': page,
        'page_size': page_size,
        'ordering': ordering,
        'key': api_key}
    
    path = config.API_LEGO_URL + "sets/"
    
    return request(path, parameters)


def get_set(set_id, api_key=None):
    """
    Gets details about specific set.
    
    Args:
        set_id: str or int
            Rebrickable set ID.
        
        api_key: str or None
            Rebrickable API access key. If set to None the one set by
            rebrick.init() is used.
    
    Returns:
        http.client.HTTPResponse
            Server response.
    """
    
    if '-' not in str(set_id):
        set_id = "%s-1" % set_id
    
    parameters = {'key': api_key}
    
    path = config.API_LEGO_URL + "sets/%s/" % set_id
    
    return request(path, parameters)


def get_set_alternates(set_id, page=None, page_size=None, ordering=None, api_key=None):
    """
    Gets details about available alternate builds for specific set.
    
    Args:
        set_id: str or int
            Rebrickable set ID.
        
        page: int or None
            A page number within the paginated result set.
        
        page_size: int or None
            Number of results to return per page.
        
        ordering: str or None
            Specifies the field to use for results ordering.
        
        api_key: str or None
            Rebrickable API access key. If set to None the one set by
            rebrick.init() is used.
    
    Returns:
        http.client.HTTPResponse
            Server response.
    """
    
    if '-' not in str(set_id):
        set_id = "%s-1" % set_id
    
    parameters = {
        'page': page,
        'page_size': page_size,
        'ordering': ordering,
        'key': api_key}
    
    path = config.API_LEGO_URL + "sets/%s/alternates/" % set_id
    
    return request(path, parameters)


def get_set_elements(set_id, part_details=False, color_details=True, minifig_parts=False, page=None, page_size=None, ordering=None, api_key=None):
    """
    Gets details about available elements for specific set.
    
    Args:
        set_id: str or int
            Rebrickable set ID.
        
        part_details: bool
            If set to True part details will be retrieved.
        
        color_details: bool
            If set to True color details will be retrieved.
        
        minifig_parts: bool
            If set to True, minifig parts wil be retrieved.
        
        page: int or None
            A page number within the paginated result set.
        
        page_size: int or None
            Number of results to return per page.
        
        ordering: str or None
            Specifies the field to use for results ordering.
        
        api_key: str or None
            Rebrickable API access key. If set to None the one set by
            rebrick.init() is used.
    
    Returns:
        http.client.HTTPResponse
            Server response.
    """
    
    if '-' not in str(set_id):
        set_id = "%s-1" % set_id
    
    parameters = {
        'inc_part_details': int(part_details),
        'inc_color_details': int(color_details),
        'inc_minifig_parts': int(minifig_parts),
        'page': page,
        'page_size': page_size,
        'ordering': ordering,
        'key': api_key}
    
    path = config.API_LEGO_URL + "sets/%s/parts/" % set_id
    
    return request(path, parameters)


def get_set_minifigs(set_id, page=None, page_size=None, ordering=None, api_key=None):
    """
    Gets details about available minifigs for specific set.
    
    Args:
        set_id: str or int
            Rebrickable set ID.
        
        page: int or None
            A page number within the paginated result set.
        
        page_size: int or None
            Number of results to return per page.
        
        ordering: str or None
            Specifies the field to use for results ordering.
        
        api_key: str or None
            Rebrickable API access key. If set to None the one set by
            rebrick.init() is used.
    
    Returns:
        http.client.HTTPResponse
            Server response.
    """
    
    if '-' not in str(set_id):
        set_id = "%s-1" % set_id
    
    parameters = {
        'page': page,
        'page_size': page_size,
        'ordering': ordering,
        'key': api_key}
    
    path = config.API_LEGO_URL + "sets/%s/minifigs/" % set_id
    
    return request(path, parameters)


def get_themes(page=None, page_size=None, ordering=None, api_key=None):
    """
    Gets details for all available set themes.
    
    Args:
        page: int or None
            A page number within the paginated result set.
        
        page_size: int or None
            Number of results to return per page.
        
        ordering: str or None
            Specifies the field to use for results ordering.
        
        api_key: str or None
            Rebrickable API access key. If set to None the one set by
            rebrick.init() is used.
    
    Returns:
        http.client.HTTPResponse
            Server response.
    """
    
    parameters = {
        'page': page,
        'page_size': page_size,
        'ordering': ordering,
        'key': api_key}
    
    path = config.API_LEGO_URL + "themes/"
    
    return request(path, parameters)


def get_theme(theme_id, api_key=None):
    """
    Gets details about specific set theme.
    
    Args:
        theme_id: str or int
            Rebrickable theme ID.
        
        api_key: str or None
            Rebrickable API access key. If set to None the one set by
            rebrick.init() is used.
    
    Returns:
        http.client.HTTPResponse
            Server response.
    """
    
    parameters = {'key': api_key}
    
    path = config.API_LEGO_URL + "themes/%s/" % theme_id
    
    return request(path, parameters)
