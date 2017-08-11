import { Component } from '@angular/core';

@Component({
    selector: 'app-dashboard',
    moduleId: module.id,
    templateUrl: 'dashboard.component.html'
})
export class Dashboard{
    private title = "Bucketlist";

    onLogout(){
        // remove token and refresh
        localStorage.clear();
        window.location.reload();
    }
}
