#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This file is part of the django ERP project.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

__author__ = 'Emanuele Bertoldi <emanuele.bertoldi@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Emanuele Bertoldi'
__version__ = '0.0.2'

from djangoerp.pluggets.loading import register_plugget

from utils import get_bookmarks_for
from models import Menu

def menu(context):
    """Menu plugget.
    
    Simply renders a menu.
    """
    """
    It adds a context variables:
    
     * name -- Slug of selected menu.
    """
    pk = context.pop(u'menu_id', None)
    if pk:
        menu = Menu.objects.get(pk=pk)
        context["name"] = menu.slug
    return context
    
def bookmarks_menu(context):
    """Bookmarks plugget.
    
    Shows all your bookmarks.
    """
    if 'user' in context:
        context[u'menu_id'] = get_bookmarks_for(context['user'].username).pk  
    return menu(context)
