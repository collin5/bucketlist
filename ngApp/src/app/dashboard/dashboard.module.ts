import { NgModule } from '@angular/core';
import { Dashboard } from './dashboard.component';
import { SharedModule } from '../shared/shared.module';
import { Bucketlists } from './bucketlists/bucketlist.component';

@NgModule({
    declarations: [
        Dashboard, Bucketlists
    ],
    imports: [
        SharedModule
    ],
    providers: []
})
export class DashboardModule{}

