from pywebcopy import save_website

def update_website(project_name, project_folder, url):
    kwargs = {'project_name': project_name, 'over_write': True, 'bypass_robots': True, 'zip_project_folder': False,
              'debug': True}
    try:
        save_website(
            url=url,
            project_folder=project_folder,
            **kwargs
        )
        return True
    except:
        return False
