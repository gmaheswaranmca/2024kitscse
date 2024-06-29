import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class BackendCallsService {
  baseUrl = "http://localhost:5000"
  constructor(private backend:HttpClient) { 

  }

  readAll() {
    return this.backend.get(`${this.baseUrl}/vendors`)
  }
  readById(id:any) { 
    return this.backend.get(`${this.baseUrl}/vendors/${id}`)
  }
  create(vendor:any) { 
    return this.backend.post(`${this.baseUrl}/vendors`,vendor)
  }
  update(id:any,vendor:any) { 
    return this.backend.put(`${this.baseUrl}/vendors/${id}`,vendor)
  }
  delete(id:any) { 
    return this.backend.delete(`${this.baseUrl}/vendors/${id}`)
  }
}
