import { Component } from '@angular/core';

@Component({
    selector: 'bt-info',
    moduleId: module.id,
    templateUrl: 'bucket-info.component.html'
})
export class BucketInfoComponent{
    title: string = "Bucket info";
    bucket_title: string = "Bucket title";
}
