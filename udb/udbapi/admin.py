# -*- encoding: utf-8 -*-
# Copyright (c) 2013 Pierre Bourdon <pierre.bourdon@prologin.org>
# Copyright (c) 2013 Association Prologin <info@prologin.org>
#
# Prologin-SADM is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Prologin-SADM is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Prologin-SADM.  If not, see <http://www.gnu.org/licenses/>.

from django.contrib import admin
from udbapi import models


def root(request):
    if not request.user.is_authenticated():
        return False
    try:
        request.user.groups.get(name='root')
    except Exception as e:
        return False
    return True


class UserAdmin(admin.ModelAdmin):
    list_display = ('login', 'group', 'curr_machine')
    list_filter = ('group',)
    list_per_page = 250
    radio_fields = { 'group': admin.HORIZONTAL }
    search_fields = ('login', 'curr_machine')

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True  # Let every organizer access the list
        return root(request) or obj.group != 'root'


admin.site.register(models.User, UserAdmin)
