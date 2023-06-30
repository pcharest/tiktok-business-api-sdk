# coding: utf-8

"""
 Copyright 2023 TikTok Pte. Ltd.

 This source code is licensed under the MIT license found in
 the LICENSE file in the root directory of this source tree.
"""
import pprint
import re  # noqa: F401

import six

class AdAcoBodyMediaInfoImageInfo(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'file_name': 'str',
        'web_uri': 'str'
    }

    attribute_map = {
        'file_name': 'file_name',
        'web_uri': 'web_uri'
    }

    def __init__(self, file_name=None, web_uri=None):  # noqa: E501
        """AdAcoBodyMediaInfoImageInfo - a model defined in Swagger"""  # noqa: E501
        self._file_name = None
        self._web_uri = None
        self.discriminator = None
        if file_name is not None:
            self.file_name = file_name
        if web_uri is not None:
            self.web_uri = web_uri

    @property
    def file_name(self):
        """Gets the file_name of this AdAcoBodyMediaInfoImageInfo.  # noqa: E501

        Image name. If image material is used, this field is used to form ad's name.  # noqa: E501

        :return: The file_name of this AdAcoBodyMediaInfoImageInfo.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this AdAcoBodyMediaInfoImageInfo.

        Image name. If image material is used, this field is used to form ad's name.  # noqa: E501

        :param file_name: The file_name of this AdAcoBodyMediaInfoImageInfo.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def web_uri(self):
        """Gets the web_uri of this AdAcoBodyMediaInfoImageInfo.  # noqa: E501

        Image ID. You can find the image ID in the response after you upload an image via the [/file/image/ad/upload/](https://ads.tiktok.com/marketing_api/docs?id=1739067433456642) endpoint.  # noqa: E501

        :return: The web_uri of this AdAcoBodyMediaInfoImageInfo.  # noqa: E501
        :rtype: str
        """
        return self._web_uri

    @web_uri.setter
    def web_uri(self, web_uri):
        """Sets the web_uri of this AdAcoBodyMediaInfoImageInfo.

        Image ID. You can find the image ID in the response after you upload an image via the [/file/image/ad/upload/](https://ads.tiktok.com/marketing_api/docs?id=1739067433456642) endpoint.  # noqa: E501

        :param web_uri: The web_uri of this AdAcoBodyMediaInfoImageInfo.  # noqa: E501
        :type: str
        """

        self._web_uri = web_uri

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AdAcoBodyMediaInfoImageInfo, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AdAcoBodyMediaInfoImageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other