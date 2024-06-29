import { Component } from '@angular/core';
import { BackendCallsService } from '../backend-calls.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-vendor-create',
  templateUrl: './vendor-create.component.html',
  styleUrl: './vendor-create.component.css'
})
export class VendorCreateComponent {
  vendor = {
    name:'',
    ratings:1,
    place:'',
    phone_number:''
  };
  constructor(private backend:BackendCallsService,
    private _router:Router
  ) {
  }


  doCreate() {
    this.backend.create(this.vendor)
      .subscribe({
        next:(vendor)=>{
          console.log(vendor)
          this._router.navigate(['vendors/list'])
        }, 
        error:(err)=>{
          console.log(err)
        }       
      })
  }
}
//id=+this._route.snapshot.paramMap.get('id')     private _route: ActivatedRoute
//this.router.navigate(['role']);                 private router: Router      