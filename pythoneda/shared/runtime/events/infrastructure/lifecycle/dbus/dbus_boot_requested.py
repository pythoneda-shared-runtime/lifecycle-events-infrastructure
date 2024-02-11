# vim: set fileencoding=utf-8
"""
pythoneda/shared/runtime/events/infrastructure/lifecycle/dbus/dbus_boot_requested.py

This file defines the DbusBootRequested class.

Copyright (C) 2024-today rydnr's pythoneda-shared-runtime/lifecycle-events-infrastructure

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from dbus_next import Message
from dbus_next.service import ServiceInterface, signal
import json
from pythoneda.shared import BaseObject
from pythoneda.shared.runtime.events.lifecycle import BootRequested
from pythoneda.shared.runtime.events.infrastructure.lifecycle.dbus import DBUS_PATH
from typing import List


class DbusBootRequested(BaseObject, ServiceInterface):
    """
    D-Bus interface for BootRequested.

    Class name: DbusBootRequested

    Responsibilities:
        - Define the d-bus interface for the BootRequested event.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new DbusBootRequested.
        """
        super().__init__("Pythoneda_Shared_Runtime_Events_Lifecycle_BootRequested")

    @signal()
    def BootRequested(self, defUrl: "s"):
        """
        Defines the BootRequested d-bus signal.
        :param defUrl: The url of the definition repository.
        :type defUrl: str
        """
        pass

    @classmethod
    def path(cls) -> str:
        """
        Retrieves the d-bus path.
        :return: Such value.
        :rtype: str
        """
        return DBUS_PATH

    @classmethod
    def transform(cls, event: BootRequested) -> List[str]:
        """
        Transforms given event to signal parameters.
        :param event: The event to transform.
        :type event: pythoneda.shared.runtime.events.lifecycle.BootRequested
        :return: The event information.
        :rtype: List[str]
        """
        return [
            event.url,
            event.id,
            json.dumps(event.previous_event_ids),
        ]

    @classmethod
    def sign(cls, event: BootRequested) -> str:
        """
        Retrieves the signature for the parameters of given event.
        :param event: The domain event.
        :type event: pythoneda.shared.runtime.events.lifecycle.BootRequested
        :return: The signature.
        :rtype: str
        """
        return "sss"

    @classmethod
    def parse(cls, message: Message) -> BootRequested:
        """
        Parses given d-bus message containing a BootRequested event.
        :param message: The message.
        :type message: dbus_next.Message
        :return: The BootRequested event.
        :rtype: pythoneda.shared.runtime.events.lifecycle.BootRequested
        """
        url, event_id, prev_event_ids = message.body
        return BootRequested(
            url,
            None,
            event_id,
            json.loads(prev_event_ids),
        )


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
