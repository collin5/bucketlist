import { NgModule } from '@angular/core';
import { Dashboard } from './dashboard.component';
import { SharedModule } from '../shared/shared.module';
import { Bucketlists } from './bucketlists/bucketlist.component';
import { Bucket } from './bucketlists/bucket.component';
import { KeysPipe } from './bucketlists/convert_to_keys.pipe';

@NgModule({
    declarations: [
        Dashboard, Bucketlists, Bucket, KeysPipe
    ],
    imports: [
        SharedModule
    ],
    providers: []
})
export class DashboardModule{}

