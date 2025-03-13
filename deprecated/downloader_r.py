

from time import sleep
from pathlib import Path
from threading import Thread
from sys import exit, platform
from subprocess import Popen, run
# from traceback import print_exc


try:
    from requests import Session
except (ImportError, ModuleNotFoundError):
    print("\nModules are not installed!")
    exit("Run 'pip install requirements.txt' in the terminal to fix errors.")


if platform not in ("darwin", "linux", "win32"):
    exit("OS configurations not available yet.")


def clear() -> int:
    return run(args=["cls" if platform == "win32" else "clear"], shell=True if platform == "win32" else False)


class CND:
    """
    Handles general appointment functionalities.
    """
    def __init__(self, name: str, url: str) -> None:
        self.name = name
        self.url = url

        self.initial_headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
        }

        self.session_headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
        }

        self.download_headers = {
            'Accept': 'text/html, */*; q=0.01',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://appcnd.enee.hn:3200',
            'Referer': 'https://appcnd.enee.hn:3200/odsprd/f?p=110:4:::::p4_id:5',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
        }

        self.download_data = {
            'p_flow_id': '110',
            'p_flow_step_id': '4',
            'p_instance': '1343491990601',
            'p_debug': '',
            'p_request': 'PLUGIN=UkVHSU9OIFRZUEV-fjY5MjY3NjIwMjYxMjM5NjA1/ODXitFg0CrslKTz4_R9XHArdH65u7KpeFJxe0Lj9SV5FkUs0tYQ86LJjKWy_FvqNPYQe6gic6akLfu0vxBySeA',
            'p_widget_name': 'worksheet',
            'p_widget_mod': 'PULL',
            'p_widget_num_return': '25',
            'x01': '69268077341239605',
            'x02': '69271490979258662',
            'p_json': '{"pageItems":null,"salt":"93914732321180664324810614279938194830"}',
        }


    def initialize(self, session: Session) -> tuple[bool, None | dict]:
        """
        Reviews checkins and reservations.
        """
        response = session.get(self.url, headers=self.initial_headers)
        # response_dict = response.json()

        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            return False, None
        
        print(response.text)
        return
        
        if response_dict["status"] != 200:
            print(response_dict["status"])
            return False, None
        
        return True, response_dict

        # ===== Response examples =====


    def get_session_id(self, session: Session) -> tuple[bool, None | dict]:
        """
        Reviews checkins and reservations.
        """
        response = session.get(self.url, headers=self.session_headers)
        # response_dict = response.json()

        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            return False, None
        
        print(response.text)
        return
        
        if response_dict["status"] != 200:
            print(response_dict["status"])
            return False, None
        
        return True, response_dict

        # ===== Response examples =====

        """
        <!DOCTYPE html>
        <html class="no-js  page-4 app-INFORMES-ODS" lang="es-hn">
            <head>
                <meta http-equiv="x-ua-compatible" content="IE=edge"/>
                <meta charset="utf-8">
                <title>Listado website</title>
                <link rel="stylesheet" href="/i/libraries/oraclejet/15.0.7/css/libs/oj/15.0.7/redwood/oj-redwood-notag-min.css?v=23.2.0" type="text/css"/>
                <link rel="stylesheet" href="/i/app_ui/css/Core.min.css?v=23.2.0" type="text/css"/>
                <link rel="stylesheet" href="/i/app_ui/css/Theme-Standard.min.css?v=23.2.0" type="text/css"/>
                <link rel="stylesheet" href="/i/libraries/font-apex/2.2.1/css/font-apex.min.css?v=23.2.0" type="text/css"/>
                <link rel="stylesheet" href="/i/themes/theme_42/21.2/css/Core.min.css?v=23.2.0" type="text/css"/>
                <link rel="stylesheet" href="/i/themes/theme_42/21.2/css/Vita.min.css?v=23.2.0" type="text/css"/>
                <link rel="stylesheet" href="r/ods_prd/110/files/static/v3/app-icon.css?version=Release%201.0" type="text/css"/>
                <style type="text/css">
                    .t-Header,.t-Footer {
                        display: none;
                    }
                </style>
                <link rel="icon" href="/i/favicon.ico"/>
                <link rel="apple-touch-icon" href="/i/favicon-180x180.png"/>
                <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
                <meta http-equiv="Pragma" content="no-cache"/>
                <meta http-equiv="Expires" content="-1"/>
                <meta http-equiv="Cache-Control" content="no-cache"/>
                <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
            </head>
            <body class="t-PageBody t-PageBody--hideLeft t-PageBody--hideActions no-anim t-PageTemplate--standard   apex-side-nav apex-icons-fontapex apex-theme-vita" id="t_PageBody">
                <a href="#main" id="t_Body_skipToContent">Skip to Main Content</a>
                <form role="none" action="wwv_flow.accept?p_context=110:4:1343491990601" method="post" name="wwv_flow" id="wwvFlowForm" data-oj-binding-provider="none" novalidate autocomplete="off">
                    <input type="hidden" name="p_flow_id" value="110" id="pFlowId"/>
                    <input type="hidden" name="p_flow_step_id" value="4" id="pFlowStepId"/>
                    <input type="hidden" name="p_instance" value="1343491990601" id="pInstance"/>
                    <input type="hidden" name="p_page_submission_id" value="93914732321180664324810614279938194830" id="pPageSubmissionId"/>
                    <input type="hidden" name="p_request" value="" id="pRequest"/>
                    <input type="hidden" name="p_reload_on_submit" value="S" id="pReloadOnSubmit"/>
                    <input type="hidden" value="110&#x3A;4&#x3A;1343491990601" id="pContext"/>
                    <input type="hidden" value="93914732321180664324810614279938194830" id="pSalt"/>
                    <header class="t-Header" id="t_Header" role="banner">
                        <div class="t-Header-branding">
                            <div class="t-Header-controls">
                                <button class="t-Button t-Button--icon t-Button--header t-Button--headerTree" aria-label="Main Navigation" title="Main Navigation" id="t_Button_navControl" type="button">
                                    <span class="t-Header-controlsIcon" aria-hidden="true"></span>
                                </button>
                            </div>
                            <div class="t-Header-logo">
                                <a href="f?p=110:4::::::" class="t-Header-logo-link">
                                    <span class="apex-logo-text">Informes ODS</span>
                                </a>
                            </div>
                            <div class="t-Header-navBar">
                                <div class="t-Header-navBar--start"></div>
                                <div class="t-Header-navBar--center">
                                    <ul class="t-NavigationBar " id="50360349553632428">
                                        <li class="t-NavigationBar-item icon-only">
                                            <button class="t-Button t-Button--icon t-Button t-Button--header t-Button--navBar js-menuButton" type="button" id="L50372709634632439" data-menu="menu_L50372709634632439" title="">
                                                <span class="t-Icon fa&#x20;fa-question-circle-o" aria-hidden="true"></span>
                                                <span class="t-Button-label">About</span>
                                                <span class="t-Button-badge"></span>
                                                <span class="a-Icon icon-down-arrow" aria-hidden="true"></span>
                                            </button>
                                            <div class="t-NavigationBar-menu" style="display: none" id="menu_L50372709634632439">
                                                <ul>
                                                    <li data-current="false" data-icon="fa&#x20;fa-question-circle-o">
                                                        <a href="javascript:apex.theme42.dialog('f?p=110:10011:1343491990601::::P10011_PAGE_ID:4\u0026cs=3vHh_xIkAMfioBwIYTjKC8yn5O-QRZ9xQPUpyygfOPmdAw58mRvu_jr4JWu5569eXmenhyb1gZDv8kUXwruX4kA\u0026p_dialog_cs=BNuBZ4B_qZf9srYXi7c0oZXKs8ZIaAJFFbxRyRLq3rebtzf9LbF0ac8o1yuu7NhKqrqQYiNHvNsnR0gyvB8LYw',{title:'Help',h:'auto',w:'720',mxw:'960',modal:true,dialog:null,dlgCls:'t-Dialog-page--standard '+''},'',apex.gPageContext$)" title="">Página de ayuda</a>
                                                    </li>
                                                    <li data-current="false" data-icon="">
                                                        <a href="separator" title="">---</a>
                                                    </li>
                                                    <li data-current="false" data-icon="fa&#x20;fa-info-circle-o">
                                                        <a href="f?p=110:10010:1343491990601:::10010::&cs=35lW_cavrZ5e-5ZpGWTLRcGAFLS8pQ2i-Xqku3-msovSfgYDTw2RMDSTQzPaNbl0-QsMl2QFWT6Z3QA1RXm7yaA" title="">Acerca de la página</a>
                                                    </li>
                                                </ul>
                                            </div>
                                        </li>
                                        <li class="t-NavigationBar-item has-username">
                                            <button class="t-Button t-Button--icon t-Button t-Button--header t-Button--navBar js-menuButton" type="button" id="L50374349650632440" data-menu="menu_L50374349650632440" title="">
                                                <span class="t-Icon fa&#x20;fa-user" aria-hidden="true"></span>
                                                <span class="t-Button-label">nobody</span>
                                                <span class="t-Button-badge"></span>
                                                <span class="a-Icon icon-down-arrow" aria-hidden="true"></span>
                                            </button>
                                            <div class="t-NavigationBar-menu" style="display: none" id="menu_L50374349650632440">
                                                <ul>
                                                    <li data-current="false" data-icon="">
                                                        <a href="separator" title="">---</a>
                                                    </li>
                                                    <li data-current="false" data-icon="fa&#x20;fa-sign-out">
                                                        <a href="apex_authentication.logout?p_app_id=110&p_session_id=1343491990601" title="">Cerrar sesión</a>
                                                    </li>
                                                </ul>
                                            </div>
                                        </li>
                                    </ul>
                                </div>
                                <div class="t-Header-navBar--end"></div>
                            </div>
                        </div>
                        <div class="t-Header-nav"></div>
                    </header>
                    <div class="t-Body">
                        <div class="t-Body-nav" id="t_Body_nav" role="navigation" aria-label="Main Navigation">
                            <div class="t-TreeNav js-defaultCollapsed js-defaultCollapsed js-navCollapsed--hidden t-TreeNav--styleA" id="t_TreeNav" data-id="4_tree" aria-label="Main Navigation">
                                <ul style="display:none">
                                    <li data-id="" data-disabled="" data-icon="fa&#x20;fa-home" data-shortcut="">
                                        <a href="f?p=110:1:1343491990601:::::" title="" target="">Home</a>
                                    </li>
                                    <li data-current="true" data-id="" data-disabled="" data-icon="" data-shortcut="">
                                        <a href="f?p=110:4::::::" title="" target="">Listado website</a>
                                    </li>
                                </ul>
                            </div>
                        </div>
                        <script>
                            (sessionStorage.getItem("ORA_WWV_apex.toggleCore.nav.110.preferenceForExpanded") === "true" && window.matchMedia("(min-width: " + getComputedStyle(document.documentElement).getPropertyValue("--js-mq-lg") + ")").matches) && document.getElementById('t_PageBody').classList.add('js-navExpanded');
                        </script>
                        <div class="t-Body-main">
                            <div class="t-Body-title" id="t_Body_title"></div>
                            <div class="t-Body-content" id="t_Body_content">
                                <main id="main" class="t-Body-mainContent">
                                    <span id="APEX_SUCCESS_MESSAGE" data-template-id="50200282655632366_S" class="apex-page-success u-hidden"></span>
                                    <span id="APEX_ERROR_MESSAGE" data-template-id="50200282655632366_E" class="apex-page-error u-hidden"></span>
                                    <div class="t-Body-fullContent"></div>
                                    <div class="t-Body-contentInner">
                                        <div class="container">
                                            <div class="row ">
                                                <div class="col col-12 apex-col-auto col-start col-end">
                                                    <div role="region" aria-label="Report&#x20;1" id="R69267620261239605" class="t-IRR-region ">
                                                        <input type="hidden" name="P4_ID" id="P4_ID" value="5">
                                                        <input type="hidden" data-for="P4_ID" value="fmAXxe8c5DnfeAaqFOtSDUbkGvxgKysM-Xj9a3AtabWNGAzOZalmdZigpfGv1uTzfMRGDbr0zO_XHcK8dLng_g">
                                                        <div id="R69267620261239605_ir" class="a-IRR-container">
                                                            <div id="R69267620261239605_worksheet_region" class="a-IRR" aria-live="polite">
                                                                <div id="R69267620261239605_single_row_view" class="a-IRR-singleRowView"></div>
                                                                <div id="R69267620261239605_full_view" class="a-IRR-fullView">
                                                                    <div id="R69267620261239605_actions_menu"></div>
                                                                    <div id="R69267620261239605_column_search_drop" class="a-IRR-colSearch"></div>
                                                                    <div id="R69267620261239605_toolbar" class="a-IRR-toolbar">
                                                                        <div role="search" aria-label="Search&#x20;bar&#x20;of&#x20;Report&#x20;1" id="R69267620261239605_toolbar_controls" class="a-IRR-controls">
                                                                            <div class="a-IRR-controlGroup a-IRR-controlGroup--search">
                                                                                <div class="a-IRR-search">
                                                                                    <input type="hidden" id="R69267620261239605_column_search_current_column"/>
                                                                                    <div class="a-IRR-colSelector">
                                                                                        <button id="R69267620261239605_column_search_root" data-menu="R69267620261239605_column_search_drop" class="a-Button a-IRR-button a-IRR-button--colSearch a-Button--withIcon a-Button--noLabel" title="Select&#x20;columns&#x20;to&#x20;search" aria-label="Select&#x20;columns&#x20;to&#x20;search" type="button">
                                                                                            <span class="a-Icon icon-search" aria-hidden="true"></span>
                                                                                            <span class="a-Icon icon-menu-drop-down" aria-hidden="true"></span>
                                                                                        </button>
                                                                                    </div>
                                                                                    <div class="a-IRR-searchFieldContainer">
                                                                                        <input class="a-IRR-search-field" id="R69267620261239605_search_field" title="Search Report" type="search" size="30" maxlength="4000" value=""/>
                                                                                    </div>
                                                                                    <div class="a-IRR-searchButtonContainer">
                                                                                        <button id="R69267620261239605_search_button" class="a-Button a-IRR-button a-IRR-button--search" type="button">
                                                                                            <span>Buscar</span>
                                                                                        </button>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                            <div class="a-IRR-controlGroup a-IRR-controlGroup--views"></div>
                                                                            <div class="a-IRR-controlGroup a-IRR-controlGroup--options">
                                                                                <div class="a-IRR-rowSelector">
                                                                                    <label for="R69267620261239605_row_select">Rows</label>
                                                                                    <select class="a-IRR-selectList" size="1" id="R69267620261239605_row_select" name="p_accept_processing">
                                                                                        <option value="1">1</option>
                                                                                        <option value="5">5</option>
                                                                                        <option value="10">10</option>
                                                                                        <option value="15">15</option>
                                                                                        <option value="20">20</option>
                                                                                        <option selected="selected" value="25">25</option>
                                                                                    </select>
                                                                                </div>
                                                                                <div class="a-IRR-actions">
                                                                                    <button id="R69267620261239605_actions_button" class="a-Button a-IRR-button a-IRR-button--actions" type="button" data-menu="R69267620261239605_actions_menu">
                                                                                        Actions<span aria-hidden="true" class="a-Icon icon-menu-drop-down"></span>
                                                                                    </button>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                    <div id="R69267620261239605_content" class="a-IRR-content is-loading">
                                                                        <div id="R69267620261239605_dialog_js" class="a-IRR-dialogBody" style="display:none"></div>
                                                                        <input type="hidden" id="R69267620261239605_worksheet_id" value="69268077341239605"/>
                                                                        <input type="hidden" id="R69267620261239605_app_user" value="nobody"/>
                                                                        <input type="hidden" id="R69267620261239605_report_id" value="69271490979258662"/>
                                                                        <input type="hidden" id="R69267620261239605_view_mode" value="REPORT"/>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                            <div role="dialog" aria-label="Column&#x20;Actions" aria-modal="true" class="a-IRR-sortWidget" id="R69267620261239605_sort_widget" style="display:none;">
                                                                <h1 class="u-vh" aria-roledescription="Visually&#x20;hidden&#x20;dialog&#x20;title">Column Actions</h1>
                                                                <ul role="toolbar" class="a-IRR-sortWidget-actions" id="R69267620261239605_sort_widget_actions">
                                                                    <li role="none" class="a-IRR-sortWidget-actions-item" id="R69267620261239605_sort_widget_action_up">
                                                                        <button class="a-Button a-IRR-button a-IRR-sortWidget-button" type="button" title="Sort&#x20;Ascending" aria-label="Sort&#x20;Ascending" data-option="up">
                                                                            <span aria-hidden="true" class="a-Icon icon-irr-sort-asc"></span>
                                                                        </button>
                                                                    </li>
                                                                    <li role="none" class="a-IRR-sortWidget-actions-item" id="R69267620261239605_sort_widget_action_down">
                                                                        <button class="a-Button a-IRR-button a-IRR-sortWidget-button" type="button" title="Sort&#x20;Descending" aria-label="Sort&#x20;Descending" data-option="down">
                                                                            <span aria-hidden="true" class="a-Icon icon-irr-sort-desc"></span>
                                                                        </button>
                                                                    </li>
                                                                    <li role="none" class="a-IRR-sortWidget-actions-item" id="R69267620261239605_sort_widget_action_hide">
                                                                        <button class="a-Button a-IRR-button a-IRR-sortWidget-button" type="button" title="Hide&#x20;Column" aria-label="Hide&#x20;Column" data-option="hide">
                                                                            <span aria-hidden="true" class="a-Icon icon-irr-remove-col"></span>
                                                                        </button>
                                                                    </li>
                                                                    <li role="none" class="a-IRR-sortWidget-actions-item" id="R69267620261239605_sort_widget_action_break">
                                                                        <button class="a-Button a-IRR-button a-IRR-sortWidget-button" type="button" title="Control&#x20;Break" aria-label="Control&#x20;Break" data-option="break">
                                                                            <span aria-hidden="true" class="a-Icon icon-irr-control-break"></span>
                                                                        </button>
                                                                    </li>
                                                                    <li role="none" class="a-IRR-sortWidget-actions-item" id="R69267620261239605_sort_widget_action_help">
                                                                        <button class="a-Button a-IRR-button a-IRR-sortWidget-button" type="button" title="Help" aria-label="Help" data-option="help" aria-pressed="false">
                                                                            <span aria-hidden="true" class="a-Icon icon-irr-help"></span>
                                                                        </button>
                                                                    </li>
                                                                    <li role="none" class="a-IRR-sortWidget-actions-item" id="R69267620261239605_sort_widget_action_computation">
                                                                        <button class="a-Button a-IRR-button a-IRR-sortWidget-button" type="button" title="Compute" aria-label="Compute" data-option="computation">
                                                                            <span aria-hidden="true" class="a-Icon icon-irr-calculator"></span>
                                                                        </button>
                                                                    </li>
                                                                </ul>
                                                                <div role="region" aria-label="Help" class="a-IRR-sortWidget-help" id="R69267620261239605_sort_widget_help"></div>
                                                                <div role="search" class="a-IRR-sortWidget-search" id="R69267620261239605_sort_widget_search">
                                                                    <label for="R69267620261239605_sort_widget_search_field" class="a-IRR-sortWidget-searchLabel">
                                                                        <span class="u-vh">Search</span>
                                                                    </label>
                                                                    <input id="R69267620261239605_sort_widget_search_field" class="a-IRR-sortWidget-searchField" type="text" placeholder="Filter..."/>
                                                                    <div role="group" aria-label="Filter&#x20;suggestions" class="a-IRR-sortWidget-rows" id="R69267620261239605_sort_widget_rows"></div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </main>
                                <footer class="t-Footer" id="t_Footer" role="contentinfo">
                                    <div class="t-Footer-body">
                                        <div class="t-Footer-content"></div>
                                        <div class="t-Footer-apex">
                                            <div class="t-Footer-version">Release 1.0</div>
                                            <div class="t-Footer-customize"></div>
                                        </div>
                                    </div>
                                    <div class="t-Footer-top">
                                        <a href="#top" class="t-Footer-topButton" id="t_Footer_topButton">
                                            <span class="a-Icon icon-up-chevron"></span>
                                        </a>
                                    </div>
                                </footer>
                            </div>
                        </div>
                    </div>
                    <div class="t-Body-inlineDialogs" id="t_Body_inlineDialogs"></div>
                    <input type="hidden" id="pPageFormRegionChecksums" value="&#x5B;&#x5D;">
                    <input type="hidden" id="pPageItemsRowVersion" value=""/>
                    <input type="hidden" id="pPageItemsProtected" value="UDRfSUQ&#x2F;vdcurNprV1aPtvrMCnxXdW3N9pDwo2V1GZCb6V1IePNY7kAhfvZieaMw9p1WNmvSZJjI2-G7BvCpFAI27s5XiQ"/>
                </form>
                <script>
                    var apex_img_dir = "\u002Fi\u002F";
                    var apex = {
                        env: {
                            APP_USER: "nobody",
                            APP_ID: "110",
                            APP_PAGE_ID: "4",
                            APP_SESSION: "1343491990601",
                            APP_FILES: "r\u002Fods_prd\u002F110\u002Ffiles\u002Fstatic\u002Fv3\u002F",
                            WORKSPACE_FILES: "r\u002Fods_prd\u002Ffiles\u002Fstatic\u002Fv11\u002F",
                            APEX_VERSION: "23.2.0",
                            APEX_BASE_VERSION: "23.2"
                        },
                        libVersions: {
                            ckeditor5: "36.0.0",
                            cropperJs: "1.5.13",
                            domPurify: "3.0.5",
                            fullcalendar: "6.1.8",
                            hammer: "2.0.8",
                            jquery: "3.6.4",
                            jqueryUi: "1.13.2",
                            maplibre: "2.4.0",
                            markedJs: "5.1.2",
                            prismJs: "1.29.0",
                            oraclejet: "15.0.7",
                            tinymce: "6.7.1",
                            turndown: "7.1.1",
                            monacoEditor: "0.32.1",
                            lessJs: "4.1.3"
                        }
                    };
                </script>
                <script src="/i/libraries/apex/minified/desktop_all.min.js?v=23.2.0"></script>
                <script src="wwv_flow.js_messages?p_app_id=110&p_lang=es-hn&p_version=23.2.0-21083110618"></script>
                <script src="/i/themes/theme_42/21.2/js/theme42.min.js?v=23.2.0"></script>
                <script src="/i/libraries/apex/minified/widget.treeView.min.js?v=23.2.0"></script>
                <script src="/i/libraries/apex/minified/widget.interactiveReport.min.js?v=23.2.0"></script>
                <script src="/i/libraries/apex/minified/widget.stickyTableHeader.min.js?v=23.2.0"></script>
                <script src="/i/libraries/apex/minified/widget.stickyWidget.min.js?v=23.2.0"></script>
                <script src="/i/libraries/apex/minified/item.Colorpicker.min.js?v=23.2.0"></script>
                <script src="/i/libraries/oraclejet/15.0.7/js/libs/require/require.js?v=23.2.0"></script>
                <script src="/i/libraries/apex/minified/requirejs.jetConfig.min.js?v=23.2.0"></script>
                <script src="/i/libraries/apex/minified/jetCommonBundle.min.js?v=23.2.0"></script>
                <script src="/i/libraries/apex/minified/chartBundle.min.js?v=23.2.0"></script>
                <script type="text/javascript">
                    apex.jQuery(function() {
                        apex.page.init(this, function() {
                            try {
                                (function() {
                                    apex.jQuery('body').addClass('t-PageBody--leftNav');
                                }
                                )();
                                (function() {
                                    apex.jQuery('#R69267620261239605_ir').interactiveReport({
                                        "regionId": "R69267620261239605",
                                        "rowsPerPageSelect": true,
                                        "currentRowsPerPage": 25,
                                        "maxRowsPerPage": "31",
                                        "controlBreak": false,
                                        "highlight": false,
                                        "compute": false,
                                        "aggregate": false,
                                        "chart": false,
                                        "groupBy": false,
                                        "pivot": false,
                                        "flashback": false,
                                        "saveReport": false,
                                        "help": false,
                                        "download": false,
                                        "subscription": false,
                                        "lazyLoading": true,
                                        "ajaxIdentifier": "UkVHSU9OIFRZUEV-fjY5MjY3NjIwMjYxMjM5NjA1\u002FODXitFg0CrslKTz4_R9XHArdH65u7KpeFJxe0Lj9SV5FkUs0tYQ86LJjKWy_FvqNPYQe6gic6akLfu0vxBySeA"
                                    });
                                }
                                )();
                            } catch (e) {
                                apex.debug.error(e)
                            }
                            ;apex.item.waitForDelayLoadItems().done(function() {
                                try {
                                    apex.theme42.initializePage.noSideCol();

                                    apex.page.warnOnUnsavedChanges();
                                } finally {
                                    apex.event.trigger(apex.gPageContext$, 'apexreadyend');
                                }
                                ;
                            });
                        });
                    });
                    apex.pwa.cleanup({
                        serviceWorkerPath: '\u002Fodsprd\u002Fr\u002Fods_prd\u002Finformes-ods\u002Fsw.js?v=23.2.0-21083110618\u0026lang=es-hn'
                    });
                </script>
            </body>
        </html>
        """


    def download_shii(self, session: Session) -> tuple[bool, None | dict]:
        """
        Reviews checkins and reservations.
        """
        response = session.post(
            'https://appcnd.enee.hn:3200/odsprd/wwv_flow.ajax?p_context=110:4:1343491990601',
            headers=self.download_headers,
            data=self.download_data,
        )

        response = session.get(self.url, headers=self.headers)
        # response_dict = response.json()

        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            return False, None
        
        print(response.text)
        return
        
        if response_dict["status"] != 200:
            print(response_dict["status"])
            return False, None
        
        return True, response_dict

        # ===== Response examples =====

        """
        <div id="R69267620261239605_toolbar" class="a-IRR-toolbar">
            <div role="search" aria-label="Search&#x20;bar&#x20;of&#x20;Report&#x20;1" id="R69267620261239605_toolbar_controls" class="a-IRR-controls">
                <div class="a-IRR-controlGroup a-IRR-controlGroup--search">
                    <div class="a-IRR-search">
                        <input type="hidden" id="R69267620261239605_column_search_current_column"/>
                        <div class="a-IRR-colSelector">
                            <button id="R69267620261239605_column_search_root" data-menu="R69267620261239605_column_search_drop" class="a-Button a-IRR-button a-IRR-button--colSearch a-Button--withIcon a-Button--noLabel" title="Select&#x20;columns&#x20;to&#x20;search" aria-label="Select&#x20;columns&#x20;to&#x20;search" type="button">
                                <span class="a-Icon icon-search" aria-hidden="true"></span>
                                <span class="a-Icon icon-menu-drop-down" aria-hidden="true"></span>
                            </button>
                        </div>
                        <div class="a-IRR-searchFieldContainer">
                            <input class="a-IRR-search-field" id="R69267620261239605_search_field" title="Search Report" type="search" size="30" maxlength="4000" value=""/>
                        </div>
                        <div class="a-IRR-searchButtonContainer">
                            <button id="R69267620261239605_search_button" class="a-Button a-IRR-button a-IRR-button--search" type="button">
                                <span>Buscar</span>
                            </button>
                        </div>
                    </div>
                </div>
                <div class="a-IRR-controlGroup a-IRR-controlGroup--views"></div>
                <div class="a-IRR-controlGroup a-IRR-controlGroup--options">
                    <div class="a-IRR-rowSelector">
                        <label for="R69267620261239605_row_select">Rows</label>
                        <select class="a-IRR-selectList" size="1" id="R69267620261239605_row_select" name="p_accept_processing">
                            <option value="1">1</option>
                            <option value="5">5</option>
                            <option value="10">10</option>
                            <option value="15">15</option>
                            <option value="20">20</option>
                            <option selected="selected" value="25">25</option>
                        </select>
                    </div>
                    <div class="a-IRR-actions">
                        <button id="R69267620261239605_actions_button" class="a-Button a-IRR-button a-IRR-button--actions" type="button" data-menu="R69267620261239605_actions_menu">
                            Actions<span aria-hidden="true" class="a-Icon icon-menu-drop-down"></span>
                        </button>
                    </div>
                </div>
            </div>
        </div>
        <div id="R69267620261239605_content" class="a-IRR-content ">
            <div id="R69267620261239605_dialog_js" class="a-IRR-dialogBody" style="display:none"></div>
            <input type="hidden" id="R69267620261239605_worksheet_id" value="69268077341239605"/>
            <input type="hidden" id="R69267620261239605_app_user" value="nobody"/>
            <input type="hidden" id="R69267620261239605_report_id" value="69271490979258662"/>
            <input type="hidden" id="R69267620261239605_view_mode" value="REPORT"/>
            <style id="R69267620261239605_worksheet_css" type="text/css"></style>
            <div role="region" aria-label="Chart&#x20;view&#x20;of&#x20;Report&#x20;1" id="R69267620261239605_chart" class="a-IRR-chartView"></div>
            <div role="region" aria-label="Group&#x20;by&#x20;view&#x20;of&#x20;Report&#x20;1" id="R69267620261239605_group_by" class="a-IRR-groupByView"></div>
            <div role="region" aria-label="Pivot&#x20;view&#x20;of&#x20;Report&#x20;1" id="R69267620261239605_pivot" class="a-IRR-pivotView"></div>
            <div role="region" aria-label="Data&#x20;view&#x20;of&#x20;Report&#x20;1" id="R69267620261239605_data_panel" class="a-IRR-reportView">
                <div role="region" aria-label="Pagination&#x20;of&#x20;Report&#x20;1" class="a-IRR-paginationWrap a-IRR-paginationWrap--top">
                    <ul class="a-IRR-pagination">
                        <li aria-hidden="true" class="a-IRR-pagination-item is-disabled"></li>
                        <li class="a-IRR-pagination-item">
                            <span class="a-IRR-pagination-label">1 -                   25</span>
                        </li>
                        <li class="a-IRR-pagination-item">
                            <button type="button" class="a-Button a-IRR-button a-IRR-button--pagination" aria-controls="R69267620261239605" title="Next" aria-label="Next" data-pagination="pgR_min_row=26max_rows=25rows_fetched=25">
                                <span class="a-Icon icon-right-chevron" aria-hidden="true"></span>
                            </button>
                        </li>
                    </ul>
                </div>
                <div class="a-IRR-tableContainer">
                    <table aria-label="Report&#x20;1,&#x20;Report&#x20;&#x3D;&#x20;Primary&#x20;Default,&#x20;View&#x20;&#x3D;&#x20;Report" class="a-IRR-table" id="69268077341239605">
                        <tr>
                            <th class="a-IRR-header u-tC" id="C35866844846336235">
                                <a aria-haspopup="dialog" class="a-IRR-headerLink" data-column="35866844846336235" href="#">INFORME</a>
                            </th>
                            <th class="a-IRR-header u-tL" id="C50755707921965645">
                                <a aria-haspopup="dialog" class="a-IRR-headerLink" data-column="50755707921965645" href="#">DESCARGAR</a>
                            </th>
                            <th class="a-IRR-header u-tC" id="C46680261904310257">
                                <a aria-haspopup="dialog" class="a-IRR-headerLink" data-column="46680261904310257" href="#">FECHA DE PUBLICACIÓN</a>
                            </th>
                        </tr>
                        <tr>
                            <td class=" u-tL" headers="C35866844846336235">Predespacho semanal 17 &#x2F;02 &#x2F;2025 al 23 &#x2F;02 &#x2F;2025</td>
                            <td class=" u-tL" headers="C50755707921965645">
                                <a download href="apex_util.get_blob?s=1343491990601&a=110&c=50755707921965645&p=4&k1=12485&k2=&ck=6fEd8rSizOodydWF4eYVhDoVwpsOBjodBZfqtIAsZEX5fyXuKJsiSucT3ByK0WYianUzUbDNFmRKm7vjgtUIyA&rt=IR" alt="Descargar" title="Descargar 281KB">Descargar</a>
                            </td>
                            <td class=" u-tC" headers="C46680261904310257">15.02.2025</td>
                        </tr>
                        <tr>
                            <td class=" u-tL" headers="C35866844846336235">Predespacho semanal 10 &#x2F;02 &#x2F;2025 al 16 &#x2F;02 &#x2F;2025</td>
                            <td class=" u-tL" headers="C50755707921965645">
                                <a download href="apex_util.get_blob?s=1343491990601&a=110&c=50755707921965645&p=4&k1=12430&k2=&ck=gdURKeGig9Q_G-bkNBVj0CNkVW9HpgXqiRuOAHSkz2E4X5cp1_RuDmmWULetzWI2YwS0Lv1-Yr-tBgMs4siV4g&rt=IR" alt="Descargar" title="Descargar 278KB">Descargar</a>
                            </td>
                            <td class=" u-tC" headers="C46680261904310257">07.02.2025</td>
                        </tr>
                        <tr>
                            <td class=" u-tL" headers="C35866844846336235">Predespacho semanal 03 &#x2F;02 &#x2F;2025 al 09 &#x2F;02 &#x2F;2025_ACT</td>
                            <td class=" u-tL" headers="C50755707921965645">
                                <a download href="apex_util.get_blob?s=1343491990601&a=110&c=50755707921965645&p=4&k1=12387&k2=&ck=tyAHdLVJcWZMuTq-tzRFHVhROY23MLpE4KSFAO_yx83YpFcPuMipmuu4CBRAGF6e_iKJge-XpiJ96JrBVQK4wA&rt=IR" alt="Descargar" title="Descargar 279KB">Descargar</a>
                            </td>
                            <td class=" u-tC" headers="C46680261904310257">02.02.2025</td>
                        </tr>
                        <tr>
                            <td class=" u-tL" headers="C35866844846336235">Predespacho semanal 03 &#x2F;02 &#x2F;2025 al 09 &#x2F;02 &#x2F;2025</td>
                            <td class=" u-tL" headers="C50755707921965645">
                                <a download href="apex_util.get_blob?s=1343491990601&a=110&c=50755707921965645&p=4&k1=12378&k2=&ck=OnzsMNp7O_tMOT_CVnez94Y5hNZI13gDv6LenLa1uDf3aZeTk3R3tStAtIZN1qtrv9Cb1mS9ADDF7ievYcJdfQ&rt=IR" alt="Descargar" title="Descargar 260KB">Descargar</a>
                            </td>
                            <td class=" u-tC" headers="C46680261904310257">31.01.2025</td>
                        </tr>
                        <tr>
                            <td class=" u-tL" headers="C35866844846336235">Predespacho semanal 27 &#x2F;01 &#x2F;2025 al 02 &#x2F;02 &#x2F;2025</td>
                            <td class=" u-tL" headers="C50755707921965645">
                                <a download href="apex_util.get_blob?s=1343491990601&a=110&c=50755707921965645&p=4&k1=12328&k2=&ck=zgmf57PmQYP76bmq5mg3YHybIxYz6NBccgaDS8M8dEMZttmY4YVTiXaGt2soGAk5m5_E-G0dOmJWp-Mdky4BoQ&rt=IR" alt="Descargar" title="Descargar 281KB">Descargar</a>
                            </td>
                            <td class=" u-tC" headers="C46680261904310257">24.01.2025</td>
                        </tr>
                        <tr>
                            <td class=" u-tL" headers="C35866844846336235">Predespacho semanal 20 &#x2F;01 &#x2F;2025 al 26 &#x2F;01 &#x2F;2025</td>
                            <td class=" u-tL" headers="C50755707921965645">
                                <a download href="apex_util.get_blob?s=1343491990601&a=110&c=50755707921965645&p=4&k1=12277&k2=&ck=oBENd5s-KC-hlAcCt3zYQLtcmRysfZepGvVRtYIRnTuF7mN1fxiDY2Ir4s1EO2aHWGtdxaspZgzXDOQFiQsM6Q&rt=IR" alt="Descargar" title="Descargar 278KB">Descargar</a>
                            </td>
                            <td class=" u-tC" headers="C46680261904310257">17.01.2025</td>
                        </tr>
                        <tr>
                            <td class=" u-tL" headers="C35866844846336235">Predespacho semanal 13 &#x2F;01 &#x2F;2025 al 19 &#x2F;01 &#x2F;2025</td>
                            <td class=" u-tL" headers="C50755707921965645">
                                <a download href="apex_util.get_blob?s=1343491990601&a=110&c=50755707921965645&p=4&k1=12224&k2=&ck=Wjn-3Dp81_7QXPsDEk58YFW_81shY_BMP2s2CFiwI7m5OkhBgNH9_LrbwpG2MZGp_JHiV6H2Bpcar30mS5Lw5g&rt=IR" alt="Descargar" title="Descargar 277KB">Descargar</a>
                            </td>
                            <td class=" u-tC" headers="C46680261904310257">10.01.2025</td>
                        </tr>
                        <tr>
                            <td class=" u-tL" headers="C35866844846336235">Predespacho semanal 06 &#x2F;01 &#x2F;2025 al 12 &#x2F;01 &#x2F;2025</td>
                            <td class=" u-tL" headers="C50755707921965645">
                                <a download href="apex_util.get_blob?s=1343491990601&a=110&c=50755707921965645&p=4&k1=12176&k2=&ck=4H3a8-j-3ub6yGj43Kxb73QxMTOoTG8v0xNHEZoFm70F_3S7bWDCRPewgb_z6le-Jk09zF2exT7mYOb_javQbw&rt=IR" alt="Descargar" title="Descargar 276KB">Descargar</a>
                            </td>
                            <td class=" u-tC" headers="C46680261904310257">04.01.2025</td>
                        </tr>
                        <tr>
                            <td class=" u-tL" headers="C35866844846336235">Predespacho semanal 30 &#x2F;12 &#x2F;2024 al 05 &#x2F;01 &#x2F;2024</td>
                            <td class=" u-tL" headers="C50755707921965645">
                                <a download href="apex_util.get_blob?s=1343491990601&a=110&c=50755707921965645&p=4&k1=12114&k2=&ck=2dfXFXJgsjSVWBq5MXgTVKv6TSsKVuOhK0UFzUU3j9BCB5voHYuEwl5u4W3TDPHJyOBWp_XG5rQls8_Z1W1l7A&rt=IR" alt="Descargar" title="Descargar 277KB">Descargar</a>
                            </td>
                            <td class=" u-tC" headers="C46680261904310257">27.12.2024</td>
                        </tr>
                        <tr>
                            <td class=" u-tL" headers="C35866844846336235">Predespacho semanal 23 &#x2F;12 &#x2F;2024 al 29 &#x2F;12 &#x2F;2024</td>
                            <td class=" u-tL" headers="C50755707921965645">
                                <a download href="apex_util.get_blob?s=1343491990601&a=110&c=50755707921965645&p=4&k1=12061&k2=&ck=3v9f-n5xlCTnxW9fYVlMTuxaCB_tpZpseYmShPPhXBBVcb0PajGDPIo6ZWQ8lWTAQEtTFmKci-ZhShRS8PipUw&rt=IR" alt="Descargar" title="Descargar 281KB">Descargar</a>
                            </td>
                            <td class=" u-tC" headers="C46680261904310257">21.12.2024</td>
                        </tr>
                        <tr>
                            <td class=" u-tL" headers="C35866844846336235">Predespacho semanal 16 &#x2F;12 &#x2F;2024 al 22 &#x2F;12 &#x2F;2024_REDESPACHO</td>
                            <td class=" u-tL" headers="C50755707921965645">
                                <a download href="apex_util.get_blob?s=1343491990601&a=110&c=50755707921965645&p=4&k1=12021&k2=&ck=DbMQwk0qrHuIqz7lkwpql9vU3E-ujS_mH3gSUWFkrX-RFzuIPrtpPht1TttWMDXZTdMGU9tztWKNor4vsVz9_g&rt=IR" alt="Descargar" title="Descargar 285KB">Descargar</a>
                            </td>
                            <td class=" u-tC" headers="C46680261904310257">16.12.2024</td>
                        </tr>
                        <tr>
                            <td class=" u-tL" headers="C35866844846336235">Predespacho semanal 16 &#x2F;12 &#x2F;2024 al 22 &#x2F;12 &#x2F;2024</td>
                            <td class=" u-tL" headers="C50755707921965645">
                                <a download href="apex_util.get_blob?s=1343491990601&a=110&c=50755707921965645&p=4&k1=12011&k2=&ck=sb8RBm5e7dLjsZbPw2ntJITyK5W8OH6Yy9jhIxotukGO8x9tP46sxiriLvn2sibsMd8tL8WApqncjeXsMc6IXg&rt=IR" alt="Descargar" title="Descargar 288KB">Descargar</a>
                            </td>
                            <td class=" u-tC" headers="C46680261904310257">15.12.2024</td>
                        </tr>
                        <tr>
                            <td class=" u-tL" headers="C35866844846336235">Predespacho semanal 09 &#x2F;12 &#x2F;2024 al 15 &#x2F;12 &#x2F;2024</td>
                            <td class=" u-tL" headers="C50755707921965645">
                                <a download href="apex_util.get_blob?s=1343491990601&a=110&c=50755707921965645&p=4&k1=11939&k2=&ck=YnQ5cB7OMqRsJlvRu0w_J8ZesDS18UX4QMdLyNGtwkiU0t0x3D83NG7APRGYFirbpXVJP7ZZ-7l-7QE3309Z5w&rt=IR" alt="Descargar" title="Descargar 283KB">Descargar</a>
                            </td>
                            <td class=" u-tC" headers="C46680261904310257">06.12.2024</td>
                        </tr>
                        <tr>
                            <td class=" u-tL" headers="C35866844846336235">Predespacho semanal 02 &#x2F;12 &#x2F;2024 al 08 &#x2F;12 &#x2F;2024_REDESPACHO</td>
                            <td class=" u-tL" headers="C50755707921965645">
                                <a download href="apex_util.get_blob?s=1343491990601&a=110&c=50755707921965645&p=4&k1=11903&k2=&ck=aFnFBK3ZaecvyA96XhI96FZLy0a2wG6IF46Tujw6Ze1-PHdNT2FjUg8w5oyN-GW3r1dtHj33Z7GYqGGTyPVM8w&rt=IR" alt="Descargar" title="Descargar 282KB">Descargar</a>
                            </td>
                            <td class=" u-tC" headers="C46680261904310257">02.12.2024</td>
                        </tr>
                        <tr>
                            <td class=" u-tL" headers="C35866844846336235">Predespacho semanal 02 &#x2F;12 &#x2F;2024 al 08 &#x2F;12 &#x2F;2024</td>
                            <td class=" u-tL" headers="C50755707921965645">
                                <a download href="apex_util.get_blob?s=1343491990601&a=110&c=50755707921965645&p=4&k1=11885&k2=&ck=hLslAXZ1oLXGx9fnvqfICsPlVbabJI7h1jG4Ty64lfRqCCYISyZHRS8YUXIUWu0a0l1bH16C4W4wV9isvuDX3g&rt=IR" alt="Descargar" title="Descargar 266KB">Descargar</a>
                            </td>
                            <td class=" u-tC" headers="C46680261904310257">29.11.2024</td>
                        </tr>
                        <tr>
                            <td class=" u-tL" headers="C35866844846336235">Predespacho semanal 25 &#x2F;11 &#x2F;2024 al 01 &#x2F;12 &#x2F;2024</td>
                            <td class=" u-tL" headers="C50755707921965645">
                                <a download href="apex_util.get_blob?s=1343491990601&a=110&c=50755707921965645&p=4&k1=11838&k2=&ck=zQ1N-KREm8Yk1YZDbiKHZnNcqUxMQ_m_75Bi5Ji9iYOBlHzoSgCyh5v9x97vg5XLbg0A3vWkYQUYMiImrHfdZw&rt=IR" alt="Descargar" title="Descargar 283KB">Descargar</a>
                            </td>
                            <td class=" u-tC" headers="C46680261904310257">24.11.2024</td>
                        </tr>
                        <tr>
                            <td class=" u-tL" headers="C35866844846336235">Predespacho semanal 18 &#x2F;11 &#x2F;2024 al 24 &#x2F;11 &#x2F;2024</td>
                            <td class=" u-tL" headers="C50755707921965645">
                                <a download href="apex_util.get_blob?s=1343491990601&a=110&c=50755707921965645&p=4&k1=11746&k2=&ck=DkaWA52OD-fwzZ323k2yzATwy-AOzS58SMOiD39VkPjnPPr_lAfG2y5I_ZwPAmqNAjcafoJ6bkg-duYlHrcNxg&rt=IR" alt="Descargar" title="Descargar 283KB">Descargar</a>
                            </td>
                            <td class=" u-tC" headers="C46680261904310257">16.11.2024</td>
                        </tr>
                        <tr>
                            <td class=" u-tL" headers="C35866844846336235">Predespacho semanal 11 &#x2F;11 &#x2F;2024 al 17 &#x2F;11 &#x2F;2024</td>
                            <td class=" u-tL" headers="C50755707921965645">
                                <a download href="apex_util.get_blob?s=1343491990601&a=110&c=50755707921965645&p=4&k1=11678&k2=&ck=2_fmRDGIK8w1Q16wkSMSf-VDg-bbIFjwltD8sS3_Mm_qcpm27CHHFvevulA0KKYYBEqSOQrIlWqtvOveBwra3g&rt=IR" alt="Descargar" title="Descargar 280KB">Descargar</a>
                            </td>
                            <td class=" u-tC" headers="C46680261904310257">08.11.2024</td>
                        </tr>
                        <tr>
                            <td class=" u-tL" headers="C35866844846336235">Predespacho semanal 04 &#x2F;11 &#x2F;2024 al 10 &#x2F;11 &#x2F;2024</td>
                            <td class=" u-tL" headers="C50755707921965645">
                                <a download href="apex_util.get_blob?s=1343491990601&a=110&c=50755707921965645&p=4&k1=11631&k2=&ck=9XZ6ID8HsmivU9ttAVYelgiEjrNxAYverBBZvKe_IEEAIhyrWQOomuhyiMgCPItI_h_XsKfoUIiWqfA_T798NA&rt=IR" alt="Descargar" title="Descargar 282KB">Descargar</a>
                            </td>
                            <td class=" u-tC" headers="C46680261904310257">02.11.2024</td>
                        </tr>
                        <tr>
                            <td class=" u-tL" headers="C35866844846336235">Predespacho semanal 28 &#x2F;10 &#x2F;2024 al 03 &#x2F;11 &#x2F;2024</td>
                            <td class=" u-tL" headers="C50755707921965645">
                                <a download href="apex_util.get_blob?s=1343491990601&a=110&c=50755707921965645&p=4&k1=11558&k2=&ck=YGpdhSjTMq1vXeh-EIfHo8SAO9Hfw7xwuy3egMLS9R8Af96CiDayC13H3ZM1z9bpnIu79WOysaXvyDxYQBLPzA&rt=IR" alt="Descargar" title="Descargar 283KB">Descargar</a>
                            </td>
                            <td class=" u-tC" headers="C46680261904310257">25.10.2024</td>
                        </tr>
                        <tr>
                            <td class=" u-tL" headers="C35866844846336235">Predespacho semanal 21 &#x2F;10 &#x2F;2024 al 27 &#x2F;10 &#x2F;2024</td>
                            <td class=" u-tL" headers="C50755707921965645">
                                <a download href="apex_util.get_blob?s=1343491990601&a=110&c=50755707921965645&p=4&k1=11496&k2=&ck=al_uCEuDM_2Lh70zS9LCDoF5zbT1nUKgYmhXsYWtQ-ODVQTzBuxiW3WSEdr0cD5qzJIhKP2L0qtk_X4aZRDvPQ&rt=IR" alt="Descargar" title="Descargar 266KB">Descargar</a>
                            </td>
                            <td class=" u-tC" headers="C46680261904310257">18.10.2024</td>
                        </tr>
                        <tr>
                            <td class=" u-tL" headers="C35866844846336235">Predespacho semanal 14 &#x2F;10 &#x2F;2024 al 20 &#x2F;10 &#x2F;2024</td>
                            <td class=" u-tL" headers="C50755707921965645">
                                <a download href="apex_util.get_blob?s=1343491990601&a=110&c=50755707921965645&p=4&k1=11449&k2=&ck=h1JkGV2VtXWMwRbs4oAL0Kx4qr_I9DfDnYQOtF4JNKzwrxbfsHc5neGE9RkPTnNmrSpR16sIvb9Pb7rVbdqXYA&rt=IR" alt="Descargar" title="Descargar 264KB">Descargar</a>
                            </td>
                            <td class=" u-tC" headers="C46680261904310257">12.10.2024</td>
                        </tr>
                        <tr>
                            <td class=" u-tL" headers="C35866844846336235">Predespacho semanal 07 &#x2F;10 &#x2F;2024 al 13 &#x2F;10 &#x2F;2024</td>
                            <td class=" u-tL" headers="C50755707921965645">
                                <a download href="apex_util.get_blob?s=1343491990601&a=110&c=50755707921965645&p=4&k1=11384&k2=&ck=2RCVlDCCDJEZi71kA9oacR1waQeN-2j749CHQ855xfO38aAvKyJG7kLtRO3YfgQ82Ke-gaLZr-EYY8dNOlVDXw&rt=IR" alt="Descargar" title="Descargar 278KB">Descargar</a>
                            </td>
                            <td class=" u-tC" headers="C46680261904310257">04.10.2024</td>
                        </tr>
                        <tr>
                            <td class=" u-tL" headers="C35866844846336235">Predespacho semanal 30 &#x2F;09 &#x2F;2024 al 06 &#x2F;10 &#x2F;2024</td>
                            <td class=" u-tL" headers="C50755707921965645">
                                <a download href="apex_util.get_blob?s=1343491990601&a=110&c=50755707921965645&p=4&k1=11333&k2=&ck=opB0WSLzWHjPUiA9M_PkK-oYpdmbx5jnWLv-uzYqYcqKmzlMIJSVQ4ACSMHaJb8dOo95tmprjxrhPJ-iPqu_0Q&rt=IR" alt="Descargar" title="Descargar 267KB">Descargar</a>
                            </td>
                            <td class=" u-tC" headers="C46680261904310257">28.09.2024</td>
                        </tr>
                        <tr>
                            <td class=" u-tL" headers="C35866844846336235">Predespacho semanal 23 &#x2F;09 &#x2F;2024 al 29 &#x2F;09 &#x2F;2024</td>
                            <td class=" u-tL" headers="C50755707921965645">
                                <a download href="apex_util.get_blob?s=1343491990601&a=110&c=50755707921965645&p=4&k1=11272&k2=&ck=F1bEJaKLeRIBszuM2SMIJ8XqeSc4CtcXkCvNByuhJZvvML5ojqsvgRZnuqLIZeDDs7YTWKiF_RjGV55j8kc3NA&rt=IR" alt="Descargar" title="Descargar 257KB">Descargar</a>
                            </td>
                            <td class=" u-tC" headers="C46680261904310257">20.09.2024</td>
                        </tr>
                    </table>
                </div>
                <div role="region" aria-label="Pagination&#x20;of&#x20;Report&#x20;1" class="a-IRR-paginationWrap a-IRR-paginationWrap--bottom">
                    <ul class="a-IRR-pagination">
                        <li aria-hidden="true" class="a-IRR-pagination-item is-disabled"></li>
                        <li class="a-IRR-pagination-item">
                            <span class="a-IRR-pagination-label">1 -                   25</span>
                        </li>
                        <li class="a-IRR-pagination-item">
                            <button type="button" class="a-Button a-IRR-button a-IRR-button--pagination" aria-controls="R69267620261239605" title="Next" aria-label="Next" data-pagination="pgR_min_row=26max_rows=25rows_fetched=25">
                                <span class="a-Icon icon-right-chevron" aria-hidden="true"></span>
                            </button>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
        """


    def handler(self):
        """
        App handler.
        """
        with Session() as temp_session:

            is_already_logged_in = self.initialize(session=temp_session)

            # is_already_logged_in = self.get_session_id(session=temp_session)
            # if not is_already_logged_in:
            #     is_logged_in = self.non_browser_login(session=temp_session)
            #     if not is_logged_in:
            #         print(f"[{self.user_id}] - Login Error! Check credentials then try again.")
            #         sleep(2)
            #         raise SystemExit

            #     print(f"[{self.user_id}] - Saving session...")
            #     sleep(2)
            #     print(f"[{self.user_id}] - Done saving session.")

            # print(f"[{self.user_id} : {self.mode}] - Waiting for {self.parent_category} to be available...")
            # is_successful, parent_data = self.get_activities(session=temp_session, parent_category=self.parent_category)
            # if not is_successful:
            #     raise SystemExit

            # print(f"[{self.user_id} : {self.mode}] - Waiting for {self.current_sub_category} to be available...")
            # is_successful, sub_area_data = self.get_locations(session=temp_session, sub_category=self.current_sub_category, activity=parent_data)
            # if not is_successful:
            #     raise SystemExit

            # print(f"[{self.user_id} : {self.mode}] - Finalizing the booking process...")
            # is_successful, final_response = self.book_spot(session=temp_session, parent_activity=parent_data, sub_activity=sub_area_data)
            # if not is_successful:
            #     raise SystemExit

            # print(f"[{self.user_id} : {self.mode}] - {self.parent_category} ({self.sub_category}) spot has been secured successfully.")


# class ZOID(Thread):
#     """
#     Instantiates a new zoid thread.
#     """
#     def __init__(self, data: dict[str, str]) -> None:
#         super().__init__(daemon=True)
#         self.data = data


#     def run(self):
#         try:
#             loader(data=self.data)
#         except KeyboardInterrupt:
#             print("\nInterrupted by user!")


# def loader(data: dict[str, str]):
#     """
#     Relates zoid data to implementation.
#     """
#     try:
#         user_id = data["USER_ID"].strip()
#         password = data["PASSWORD"].strip()
#         parent_category = data["PARENT_AREA"].strip()

#         if parent_category == "Deer Hunting Parent":
#             parent_category = "Deer Hunting"

#         sub_category = data["SUB_AREA"].strip().split("/")
#         mode = data["MODE"].lower().strip()
#         cookie_folder = cookies_folder_path.joinpath(user_id)

#         match mode:
#             case "reservation":
#                 CC = RESERVATION
#             case "checkin":
#                 CC = CHECKIN
#             case _:
#                 print(f'[{user_id}] - Invalid mode: "{mode}".')
#                 sleep(2)
#                 raise SystemExit

#         CC(
#             user_id=user_id, 
#             password=password, 
#             parent_category=parent_category, 
#             sub_category=sub_category, 
#             cookie_folder=cookie_folder, 
#             mode=mode
#             ).handler()

#     except Exception as e:
#         print(e)
#         # print_exc()



if __name__ == "__main__":

    clear()
    runtime_path: Path = Path(__file__).parent
    parent_runtime_path = runtime_path.parent
    desktop_path: Path = Path("~/Desktop").expanduser()

    # Data files
    core_data_path = parent_runtime_path.joinpath("core_data")
    cookies_folder_path = core_data_path.joinpath("cookies")

    # Check for core_data folder
    if not core_data_path.is_dir():
        core_data_path.mkdir(parents=True, exist_ok=True)

    urlF = {
        "url" : "https://otr.ods.org.hn:3200/odsprd/f?p=110:4:::::p4_id:4",
        "urlx" : "https://appcnd.enee.hn:3200/odsprd/f?p=110:4:::::p4_id:4",
        "name" : "Predespacho Final",
    }

    urlS = {
        "url" : "https://otr.ods.org.hn:3200/odsprd/f?p=110:4:::::p4_id:5",
        "urlx" : "https://appcnd.enee.hn:3200/odsprd/f?p=110:4:::::p4_id:5",
        "name" : "Programación Semanal",
    }

    CND(name=urlS["name"], url=urlS["url"]).handler()

    # workers = [ZOID(data=_) for _ in (urlF, urlS)]

    # print("Spawning session...\n")
    # print("Press CTRL + C to exit.\n")

    # for worker in workers:
    #     worker.start()
    #     if worker != workers[-1]:
    #         sleep(5)

    # for worker in workers:
    #     worker.join()

    exit("Exiting.")




