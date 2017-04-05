# -*- coding: utf-8 -*-

"""
   wegene.Models.Profile

   This file was automatically generated by APIMATIC BETA v2.0 on 02/22/2016
"""
from wegene.APIHelper import APIHelper


class Profile(object):

    """Implementation of the 'profile' model.

    Genetic profile available for Wegene User

    Attributes:
        id (string): Genetic profile Id
        format (string): Genetic profile format type
        sex (string): Sex
        name (string): User real name associated with the profile

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the Profile class

        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    id -- string -- Sets the attribute id
                    format -- string -- Sets the attribute format
                    sex -- string -- Sets the attribute sex
                    name -- string -- Sets the attribute name

        """
        # Set all of the parameters to their default values
        self.id = None
        self.format = None
        self.sex = None
        self.name = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "id": "id",
            "format": "format",
            "sex": "sex",
            "name": "name",
        }

        # Parse all of the Key-Value arguments
        if kwargs is not None:
            for key in kwargs:
                # Only add arguments that are actually part of this object
                if key in replace_names:
                    setattr(self, replace_names[key], kwargs[key])

    def resolve_names(self):
        """Creates a dictionary representation of this object.

        This method converts an object to a dictionary that represents the
        format that the model should be in when passed into an API Request.
        Because of this, the generated dictionary may have different
        property names to that of the model itself.

        Returns:
            dict: The dictionary representing the object.

        """
        # Create a mapping from Model property names to API property names
        replace_names = {
            "id": "id",
            "format": "format",
            "sex": "sex",
            "name": "name",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)
