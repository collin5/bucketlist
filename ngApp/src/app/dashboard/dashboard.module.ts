import { NgModule } from '@angular/core';
import { Dashboard } from './dashboard.component';
import { SharedModule } from '../shared/shared.module';
import { Bucketlists } from './bucketlists/bucketlist.component';
import { Bucket } from './bucketlists/bucket.component';

@NgModule({
    declarations: [
        Dashboard, Bucketlists, Bucket
    ],
    imports: [
        SharedModule
    ],
    providers: []
})
export class DashboardModule{}

