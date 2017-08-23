import { NgModule } from '@angular/core';
import { Dashboard } from './dashboard.component';
import { SharedModule } from '../shared/shared.module';
import { Bucketlists } from './bucketlists/bucketlist.component';
import { Bucket } from './bucketlists/bucket.component';
import { KeysPipe } from './bucketlists/convert_to_keys.pipe';
import { RouterModule } from '@angular/router';
import { BucketInfoComponent } from './bucket/bucket-info.component';

import { DatepickerModule } from 'angular2-material-datepicker';

@NgModule({
    declarations: [
        Dashboard, Bucketlists, Bucket, KeysPipe, BucketInfoComponent
    ],
    imports: [
        SharedModule, RouterModule, DatepickerModule
    ],
    providers: []
})
export class DashboardModule{}

